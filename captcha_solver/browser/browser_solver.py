import asyncio
from pathlib import Path
from playwright.async_api import async_playwright, Page

from ..solver import CaptchaSolver


class BrowserSolver:
    def __init__(self, provider="anthropic", api_key=None, headless=True):
        self.solver = CaptchaSolver(provider=provider, api_key=api_key)
        self.headless = headless
        self._pw = None
        self._browser = None
        self.page: Page | None = None

    async def __aenter__(self):
        self._pw = await async_playwright().start()
        self._browser = await self._pw.chromium.launch(headless=self.headless)
        self.page = await self._browser.new_page()
        return self

    async def __aexit__(self, *_):
        if self._browser:
            await self._browser.close()
        if self._pw:
            await self._pw.stop()

    async def goto(self, url: str):
        await self.page.goto(url, wait_until="domcontentloaded")

    async def solve_captcha(self) -> str | list[int] | None:
        recaptcha = self.page.frame_locator("iframe[src*='recaptcha']")
        if await recaptcha.locator("body").count() > 0:
            return await self._solve_recaptcha()

        hcaptcha = self.page.frame_locator("iframe[src*='hcaptcha']")
        if await hcaptcha.locator("body").count() > 0:
            return await self._solve_hcaptcha()

        img = self.page.locator("img[src*='captcha'], img[alt*='captcha'], .captcha img")
        if await img.count() > 0:
            return await self._solve_img_captcha(img.first)

        return None

    async def _screenshot_element(self, locator) -> Path:
        tmp = Path("/tmp/captcha_shot.png")
        await locator.screenshot(path=str(tmp))
        return tmp

    async def _solve_img_captcha(self, img_locator) -> str:
        path = await self._screenshot_element(img_locator)
        result = self.solver.solve_image(path)
        inp = self.page.locator("input[name*='captcha'], input[id*='captcha'], input[placeholder*='captcha']")
        if await inp.count() > 0:
            await inp.first.fill(result.text)
        return result.text

    async def _solve_recaptcha(self) -> list[int]:
        frame = self.page.frame_locator("iframe[src*='recaptcha']")
        checkbox = frame.locator(".recaptcha-checkbox-border")
        if await checkbox.count() > 0:
            await checkbox.click()
            await asyncio.sleep(2)

        challenge = self.page.frame_locator("iframe[src*='recaptcha'][title*='challenge']")
        if await challenge.locator("body").count() > 0:
            prompt_el = challenge.locator(".rc-imageselect-desc-no-canonical, .rc-imageselect-desc")
            prompt_text = await prompt_el.inner_text() if await prompt_el.count() > 0 else "Select matching images"
            table = challenge.locator("table.rc-imageselect-table, .rc-imageselect-target")
            path = await self._screenshot_element(table)
            result = self.solver.solve_grid(path, prompt=prompt_text)
            tiles = challenge.locator("td.rc-imageselect-tile")
            for idx in result.selected:
                await tiles.nth(idx).click()
                await asyncio.sleep(0.3)
            verify = challenge.locator("#recaptcha-verify-button")
            if await verify.count() > 0:
                await verify.click()
            return result.selected
        return []

    async def _solve_hcaptcha(self) -> list[int]:
        frame = self.page.frame_locator("iframe[src*='hcaptcha']")
        checkbox = frame.locator("#checkbox")
        if await checkbox.count() > 0:
            await checkbox.click()
            await asyncio.sleep(2)

        challenge = self.page.frame_locator("iframe[src*='hcaptcha'][title*='challenge']")
        if await challenge.locator("body").count() > 0:
            prompt_el = challenge.locator(".prompt-text")
            prompt_text = await prompt_el.inner_text() if await prompt_el.count() > 0 else "Select matching images"
            grid = challenge.locator(".task-grid")
            path = await self._screenshot_element(grid)
            result = self.solver.solve_grid(path, prompt=prompt_text)
            cells = challenge.locator(".task-image")
            for idx in result.selected:
                await cells.nth(idx).click()
                await asyncio.sleep(0.3)
            submit = challenge.locator(".button-submit")
            if await submit.count() > 0:
                await submit.click()
            return result.selected
        return []
