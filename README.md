# captcha-solver 🧩

AI-powered captcha solver using vision language models. Built for AI agents that need to navigate the web autonomously.

## How it works

Uses multimodal LLMs (Claude, GPT-4V, etc.) to interpret captcha images — text recognition, object identification, puzzle solving. No ML training needed, just API calls to models that already understand images.

## Supported captcha types

- **Text captchas** — distorted text, noise, rotation
- **reCAPTCHA v2** — image grid selection ("select all traffic lights")
- **hCaptcha** — image classification challenges
- **Slider captchas** — puzzle piece alignment
- **Math captchas** — arithmetic challenges

## Install

```bash
pip install captcha-solver-ai
```

## Quick start

```python
from captcha_solver import CaptchaSolver

solver = CaptchaSolver(provider="anthropic", api_key="your-key")

# Solve a text captcha
result = solver.solve_image("captcha.png")
print(result.text)  # "xK9mP2"

# Solve reCAPTCHA grid
result = solver.solve_grid("grid.png", prompt="Select all traffic lights")
print(result.selected)  # [0, 3, 6]
```

## Browser integration

```python
from captcha_solver.browser import BrowserSolver

async with BrowserSolver(headless=True) as bot:
    await bot.goto("https://example.com/login")
    await bot.solve_captcha()  # auto-detects and solves
```

## License

MIT
