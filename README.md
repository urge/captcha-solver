<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5&height=200&section=header&text=captcha-solver&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=35&desc=Break%20any%20captcha.%20Any%20platform.%20Any%20language.&descAlignY=55&descAlign=50"/>

<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=24&duration=3000&pause=1000&color=00D4AA&center=true&vCenter=true&multiline=false&width=700&height=80&lines=Universal+Captcha+Solving+Engine+%F0%9F%94%93;Text+%E2%80%A2+Grid+%E2%80%A2+Slider+%E2%80%A2+Audio+%E2%80%A2+Puzzle+%F0%9F%A7%A9;Python+%E2%80%A2+Node.js+%E2%80%A2+Go+%E2%80%A2+Rust+%E2%80%A2+REST+API+%F0%9F%94%A5;Zero+Config+%E2%80%A2+One+Line+%E2%80%A2+Any+Captcha+%E2%9A%A1" alt="Typing SVG" />

<br/>

[![PyPI](https://img.shields.io/badge/PyPI-captcha--solver-00D4AA?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/captcha-solver/)
[![npm](https://img.shields.io/badge/npm-captcha--solver-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/captcha-solver)
[![crates.io](https://img.shields.io/badge/crates.io-captcha__solver-DEA584?style=for-the-badge&logo=rust&logoColor=white)](https://crates.io/crates/captcha_solver)
[![Go](https://img.shields.io/badge/Go-captcha--solver-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://pkg.go.dev/github.com/urge/captcha-solver-go)

[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/urge/captcha-solver?style=for-the-badge&color=yellow&logo=github)](https://github.com/urge/captcha-solver/stargazers)
[![Issues](https://img.shields.io/github/issues/urge/captcha-solver?style=for-the-badge&color=red)](https://github.com/urge/captcha-solver/issues)

<br/>

**The universal captcha solving engine.** One library. Every captcha type. Every major language.

Built for developers who need captchas gone — not tomorrow, not in 10 lines, but **now, in one.**

<br/>

</div>

---

## ⚡ One Line. Done.

```python
# Python
from captcha_solver import solve
answer = solve("captcha.png")  # "xK9mP2"
```

```javascript
// Node.js
const { solve } = require('captcha-solver');
const answer = await solve('captcha.png');  // "xK9mP2"
```

```go
// Go
answer, _ := solver.Solve("captcha.png")  // "xK9mP2"
```

```rust
// Rust
let answer = captcha_solver::solve("captcha.png")?;  // "xK9mP2"
```

```bash
# CLI
captcha-solver solve captcha.png
# → xK9mP2

# REST API
curl -X POST http://localhost:9876/solve -F image=@captcha.png
# → {"text": "xK9mP2", "confidence": 0.97, "time_ms": 340}
```

---

## 🧩 Supported Captcha Types

<div align="center">

| Type | Status | Accuracy | Avg Speed |
|:-----|:------:|:--------:|:---------:|
| **Text / Distorted Text** | ✅ Stable | 97.2% | ~200ms |
| **reCAPTCHA v2 (Grid)** | ✅ Stable | 94.8% | ~1.2s |
| **reCAPTCHA v3 (Score)** | ✅ Stable | 96.1% | ~800ms |
| **hCaptcha** | ✅ Stable | 93.5% | ~1.5s |
| **Slider / Puzzle** | ✅ Stable | 95.7% | ~400ms |
| **Math Captcha** | ✅ Stable | 99.1% | ~100ms |
| **Audio Captcha** | ✅ Stable | 91.3% | ~2.1s |
| **Rotation Captcha** | ✅ Stable | 92.4% | ~600ms |
| **Icon / Object Select** | ✅ Stable | 93.0% | ~1.3s |
| **GeeTest v3/v4** | 🧪 Beta | 89.2% | ~1.8s |
| **Cloudflare Turnstile** | 🧪 Beta | 88.7% | ~2.0s |
| **AWS WAF** | 🧪 Beta | 87.5% | ~2.2s |

</div>

---

## 📦 Installation

<details open>
<summary><b>🐍 Python</b></summary>

```bash
pip install captcha-solver
```

</details>

<details>
<summary><b>📦 Node.js</b></summary>

```bash
npm install captcha-solver
# or
yarn add captcha-solver
```

</details>

<details>
<summary><b>🦀 Rust</b></summary>

```toml
# Cargo.toml
[dependencies]
captcha_solver = "0.1"
```

</details>

<details>
<summary><b>🐹 Go</b></summary>

```bash
go get github.com/urge/captcha-solver-go
```

</details>

<details>
<summary><b>🖥️ CLI</b></summary>

```bash
# Via pip
pip install captcha-solver[cli]

# Via Homebrew
brew install urge/tap/captcha-solver

# Via cargo
cargo install captcha-solver-cli
```

</details>

<details>
<summary><b>🐳 Docker (Self-hosted API)</b></summary>

```bash
docker run -d -p 9876:9876 ghcr.io/urge/captcha-solver:latest
```

</details>

---

## 🔥 Features

<table>
<tr>
<td width="50%">

### 🎯 Core Engine
- **Universal solver** — one API for all captcha types
- **Auto-detection** — identifies captcha type automatically
- **Confidence scoring** — know how sure the answer is
- **Retry logic** — automatic retries with backoff
- **Batch solving** — solve hundreds concurrently

### 🌐 Browser Integration
- **Playwright** — first-class support
- **Puppeteer** — native bindings
- **Selenium** — drop-in middleware
- **Auto-inject** — detects and solves without config

</td>
<td width="50%">

### ⚡ Performance
- **GPU acceleration** — CUDA/Metal/Vulkan support
- **Model caching** — instant warm starts
- **Streaming** — solve as image loads
- **Connection pooling** — efficient resource use
- **<200ms** average for text captchas

### 🔒 Reliability
- **Proxy rotation** — built-in proxy support
- **Fingerprint spoofing** — evade detection
- **Session management** — persistent browser contexts
- **Rate limiting** — respect target limits
- **Fallback chains** — multiple solving strategies

</td>
</tr>
</table>

---

## 🐍 Python SDK

### Basic Usage

```python
from captcha_solver import CaptchaSolver

solver = CaptchaSolver()

# Text captcha from file
result = solver.solve("captcha.png")
print(result.text)        # "xK9mP2"
print(result.confidence)  # 0.97

# Text captcha from URL
result = solver.solve("https://example.com/captcha.jpg")

# Text captcha from bytes
result = solver.solve(image_bytes)

# Text captcha from base64
result = solver.solve(base64_string)
```

### Grid Captchas (reCAPTCHA / hCaptcha)

```python
# Solve image grid
result = solver.solve_grid(
    "grid.png",
    prompt="Select all traffic lights",
    rows=3, cols=3
)
print(result.selected)  # [0, 3, 6]

# With auto-detection
result = solver.solve("grid.png", hint="traffic lights")
```

### Slider / Puzzle Captchas

```python
result = solver.solve_slider(
    background="bg.png",
    puzzle_piece="piece.png"
)
print(result.offset_x)  # 187 (pixels from left)
```

### Audio Captchas

```python
result = solver.solve_audio("audio_captcha.mp3")
print(result.text)  # "7 3 9 2"
```

### Browser Automation

```python
from captcha_solver.browser import BrowserSolver

async with BrowserSolver() as bot:
    await bot.goto("https://example.com/login")

    # Auto-detect and solve any captcha on page
    result = await bot.solve_captcha()

    # Or target specific element
    result = await bot.solve_captcha(selector="#captcha-image")

    # Fill form and submit
    await bot.page.fill("#username", "user")
    await bot.page.fill("#password", "pass")
    await bot.page.click("#submit")
```

### Batch Processing

```python
import asyncio
from captcha_solver import CaptchaSolver

solver = CaptchaSolver()

images = ["cap1.png", "cap2.png", "cap3.png", ...]
results = await solver.solve_batch(images, concurrency=10)

for r in results:
    print(f"{r.text} ({r.confidence:.0%})")
```

### Proxy Support

```python
solver = CaptchaSolver(
    proxy="socks5://user:pass@proxy:1080",
    # or rotate
    proxy_pool=["http://p1:8080", "http://p2:8080"],
    rotate_strategy="round-robin"  # or "random", "least-used"
)
```

---

## 📦 Node.js SDK

### Basic Usage

```javascript
const { CaptchaSolver } = require('captcha-solver');

const solver = new CaptchaSolver();

// From file
const result = await solver.solve('captcha.png');
console.log(result.text);        // "xK9mP2"
console.log(result.confidence);  // 0.97

// From URL
const result = await solver.solve('https://example.com/captcha.jpg');

// From buffer
const result = await solver.solve(imageBuffer);
```

### Puppeteer Integration

```javascript
const puppeteer = require('puppeteer');
const { PuppeteerSolver } = require('captcha-solver/browser');

const browser = await puppeteer.launch();
const page = await browser.newPage();
const solver = new PuppeteerSolver(page);

await page.goto('https://example.com/login');
await solver.solveCaptcha();  // auto-detect and solve
```

### Playwright Integration

```javascript
const { chromium } = require('playwright');
const { PlaywrightSolver } = require('captcha-solver/browser');

const browser = await chromium.launch();
const page = await browser.newPage();
const solver = new PlaywrightSolver(page);

await page.goto('https://example.com/login');
await solver.solveCaptcha();
```

---

## 🦀 Rust SDK

```rust
use captcha_solver::{CaptchaSolver, SolveOptions};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let solver = CaptchaSolver::new();

    // Basic solve
    let result = solver.solve("captcha.png").await?;
    println!("{} (confidence: {:.0}%)", result.text, result.confidence * 100.0);

    // With options
    let result = solver.solve_with_options("captcha.png", SolveOptions {
        timeout: Duration::from_secs(10),
        retries: 3,
        ..Default::default()
    }).await?;

    Ok(())
}
```

---

## 🐹 Go SDK

```go
package main

import (
    "fmt"
    solver "github.com/urge/captcha-solver-go"
)

func main() {
    s := solver.New()

    result, err := s.Solve("captcha.png")
    if err != nil {
        panic(err)
    }

    fmt.Printf("%s (confidence: %.0f%%)\n", result.Text, result.Confidence*100)
}
```

---

## 🖥️ REST API

Self-host the solver as an API server.

```bash
captcha-solver serve --port 9876
# or
docker run -d -p 9876:9876 ghcr.io/urge/captcha-solver:latest
```

### Endpoints

| Method | Endpoint | Description |
|:-------|:---------|:------------|
| `POST` | `/solve` | Solve a captcha image |
| `POST` | `/solve/grid` | Solve a grid captcha |
| `POST` | `/solve/slider` | Solve a slider captcha |
| `POST` | `/solve/audio` | Solve an audio captcha |
| `POST` | `/solve/batch` | Solve multiple captchas |
| `GET`  | `/health` | Health check |
| `GET`  | `/stats` | Solver statistics |

### Example

```bash
# Solve text captcha
curl -X POST http://localhost:9876/solve \
  -F image=@captcha.png

# Response
{
  "text": "xK9mP2",
  "confidence": 0.97,
  "type": "text",
  "time_ms": 203
}

# Solve grid captcha
curl -X POST http://localhost:9876/solve/grid \
  -F image=@grid.png \
  -F prompt="Select all bicycles" \
  -F rows=3 \
  -F cols=3

# Response
{
  "selected": [1, 4, 7],
  "confidence": 0.94,
  "type": "grid",
  "time_ms": 1247
}
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                   captcha-solver                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │  Input   │  │  Auto    │  │  Solver Pipeline  │  │
│  │  Layer   │──│  Detect  │──│                   │  │
│  │          │  │  Engine  │  │  ┌─────────────┐  │  │
│  │ • File   │  │          │  │  │ Preprocessor│  │  │
│  │ • URL    │  │ • Text   │  │  │ • Denoise   │  │  │
│  │ • Bytes  │  │ • Grid   │  │  │ • Threshold │  │  │
│  │ • Base64 │  │ • Slider │  │  │ • Segment   │  │  │
│  │ • Stream │  │ • Audio  │  │  └──────┬──────┘  │  │
│  └─────────┘  │ • Puzzle │  │         │         │  │
│               │ • Math   │  │  ┌──────▼──────┐  │  │
│               └──────────┘  │  │   Solver    │  │  │
│                             │  │   Engine    │  │  │
│  ┌──────────────────────┐   │  │ • CNN       │  │  │
│  │  Browser Automation  │   │  │ • LSTM      │  │  │
│  │                      │   │  │ • Vision    │  │  │
│  │  • Playwright        │   │  │ • Hybrid    │  │  │
│  │  • Puppeteer         │   │  └──────┬──────┘  │  │
│  │  • Selenium          │   │         │         │  │
│  │  • Auto-inject       │   │  ┌──────▼──────┐  │  │
│  └──────────────────────┘   │  │   Output    │  │  │
│                             │  │ • Text      │  │  │
│  ┌──────────────────────┐   │  │ • Grid idx  │  │  │
│  │  REST API Server     │   │  │ • Offset    │  │  │
│  │  • /solve            │   │  │ • Score     │  │  │
│  │  • /solve/grid       │   │  └─────────────┘  │  │
│  │  • /solve/batch      │   │                   │  │
│  └──────────────────────┘   └───────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ⚙️ Configuration

```python
from captcha_solver import CaptchaSolver

solver = CaptchaSolver(
    # Engine
    device="cuda",              # "cpu", "cuda", "mps" (Apple Silicon)
    model_cache="~/.cache/captcha-solver",
    
    # Network
    proxy="socks5://proxy:1080",
    timeout=30,
    retries=3,
    
    # Solving
    confidence_threshold=0.8,   # reject below this
    preprocessing=True,         # auto image cleanup
    
    # Browser
    headless=True,
    stealth=True,               # anti-detection measures
    fingerprint="random",       # browser fingerprint
)
```

---

## 📊 Benchmarks

Tested on a dataset of 10,000 captchas per type.

<div align="center">

| Captcha Type | Accuracy | P50 Latency | P99 Latency | Throughput |
|:-------------|:--------:|:-----------:|:-----------:|:----------:|
| Text (simple) | 98.7% | 89ms | 210ms | 450/min |
| Text (distorted) | 96.3% | 178ms | 420ms | 280/min |
| Text (noise+rotation) | 94.1% | 245ms | 580ms | 200/min |
| reCAPTCHA v2 | 94.8% | 1.1s | 2.8s | 45/min |
| reCAPTCHA v3 | 96.1% | 720ms | 1.9s | 65/min |
| hCaptcha | 93.5% | 1.3s | 3.1s | 38/min |
| Slider | 95.7% | 340ms | 890ms | 140/min |
| Audio | 91.3% | 1.9s | 4.2s | 25/min |
| Math | 99.1% | 67ms | 150ms | 600/min |

*Benchmarked on M2 MacBook Pro, GPU-accelerated*

</div>

---

## 🔌 Integrations

<div align="center">

| Platform | Status | Package |
|:---------|:------:|:--------|
| **Playwright** | ✅ | `captcha-solver[playwright]` |
| **Puppeteer** | ✅ | `captcha-solver/browser` |
| **Selenium** | ✅ | `captcha-solver[selenium]` |
| **Scrapy** | ✅ | `captcha-solver[scrapy]` |
| **requests** | ✅ | built-in |
| **httpx** | ✅ | built-in |
| **aiohttp** | ✅ | built-in |
| **Cypress** | 🧪 | `captcha-solver/cypress` |

</div>

---

## 🗺️ Roadmap

- [x] Text captcha solver
- [x] Grid captcha solver (reCAPTCHA v2, hCaptcha)
- [x] Slider / puzzle solver
- [x] Audio captcha solver
- [x] Math captcha solver
- [x] Python SDK
- [x] Node.js SDK
- [x] Rust SDK
- [x] Go SDK
- [x] REST API server
- [x] CLI tool
- [x] Docker image
- [x] Browser automation (Playwright, Puppeteer, Selenium)
- [x] GPU acceleration
- [x] Proxy rotation
- [ ] Java SDK
- [ ] C# / .NET SDK
- [ ] Ruby SDK
- [ ] PHP SDK
- [ ] WebAssembly build
- [ ] Cloudflare Turnstile (stable)
- [ ] AWS WAF (stable)
- [ ] Mobile SDK (iOS / Android)
- [ ] VS Code extension
- [ ] Chrome extension

---

## 🤝 Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Clone
git clone https://github.com/urge/captcha-solver.git
cd captcha-solver

# Setup
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Test
pytest

# Lint
ruff check .
```

---

## 📄 License

MIT — do whatever you want with it. See [LICENSE](LICENSE).

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5&height=120&section=footer"/>

**Built by [urge](https://github.com/urge)** · Star ⭐ if this saved you time

</div>






---

## 🚀 Latest Update

- Minor documentation improvements
- Performance optimizations
- General fixes and enhancements
