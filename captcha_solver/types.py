from dataclasses import dataclass


@dataclass
class CaptchaResult:
    text: str
    confidence: float

@dataclass
class GridResult:
    selected: list[int]
    confidence: float
