import base64
from pathlib import Path

import anthropic
import openai

from .types import CaptchaResult, GridResult

PROVIDERS = {"anthropic", "openai"}

TEXT_PROMPT = """Look at this captcha image. Read the distorted text exactly as shown.
Reply with ONLY the text, nothing else. No quotes, no explanation."""

GRID_PROMPT_TEMPLATE = """This is a captcha grid image divided into a {rows}x{cols} grid.
Task: {prompt}
Number the cells 0-{max_idx} left-to-right, top-to-bottom.
Reply with ONLY a comma-separated list of cell numbers that match. Example: 0,3,6"""

SLIDER_PROMPT = """This is a slider captcha puzzle. Find the X pixel offset where the puzzle piece fits.
Reply with ONLY the number (integer pixels from left edge)."""


class CaptchaSolver:
    def __init__(self, provider: str = "anthropic", api_key: str | None = None, model: str | None = None):
        if provider not in PROVIDERS:
            raise ValueError(f"Unknown provider: {provider}. Use: {PROVIDERS}")
        self.provider = provider
        if provider == "anthropic":
            self.client = anthropic.Anthropic(api_key=api_key)
            self.model = model or "claude-sonnet-4-20250514"
        else:
            self.client = openai.OpenAI(api_key=api_key)
            self.model = model or "gpt-4o"

    def _encode_image(self, image_path: str | Path) -> tuple[str, str]:
        path = Path(image_path)
        suffix = path.suffix.lower()
        media_type = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "gif": "image/gif", "webp": "image/webp"}.get(suffix.lstrip("."), "image/png")
        data = base64.b64encode(path.read_bytes()).decode()
        return data, media_type

    def _ask_anthropic(self, image_b64: str, media_type: str, prompt: str) -> str:
        resp = self.client.messages.create(
            model=self.model, max_tokens=256,
            messages=[{"role": "user", "content": [
                {"type": "image", "source": {"type": "base64", "media_type": media_type, "data": image_b64}},
                {"type": "text", "text": prompt},
            ]}],
        )
        return resp.content[0].text.strip()

    def _ask_openai(self, image_b64: str, media_type: str, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model, max_tokens=256,
            messages=[{"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": f"data:{media_type};base64,{image_b64}"}},
                {"type": "text", "text": prompt},
            ]}],
        )
        return resp.choices[0].message.content.strip()

    def _ask(self, image_b64: str, media_type: str, prompt: str) -> str:
        if self.provider == "anthropic":
            return self._ask_anthropic(image_b64, media_type, prompt)
        return self._ask_openai(image_b64, media_type, prompt)

    def solve_image(self, image_path: str | Path) -> CaptchaResult:
        b64, mt = self._encode_image(image_path)
        text = self._ask(b64, mt, TEXT_PROMPT)
        return CaptchaResult(text=text, confidence=0.85)

    def solve_grid(self, image_path: str | Path, prompt: str, rows: int = 3, cols: int = 3) -> GridResult:
        b64, mt = self._encode_image(image_path)
        max_idx = rows * cols - 1
        full_prompt = GRID_PROMPT_TEMPLATE.format(rows=rows, cols=cols, prompt=prompt, max_idx=max_idx)
        raw = self._ask(b64, mt, full_prompt)
        selected = [int(x.strip()) for x in raw.split(",") if x.strip().isdigit()]
        return GridResult(selected=selected, confidence=0.80)

    def solve_slider(self, image_path: str | Path) -> int:
        b64, mt = self._encode_image(image_path)
        raw = self._ask(b64, mt, SLIDER_PROMPT)
        return int("".join(c for c in raw if c.isdigit()))

    def solve_math(self, image_path: str | Path) -> CaptchaResult:
        b64, mt = self._encode_image(image_path)
        prompt = "This is a math captcha. Solve the equation shown. Reply with ONLY the numeric answer."
        text = self._ask(b64, mt, prompt)
        return CaptchaResult(text=text, confidence=0.95)
