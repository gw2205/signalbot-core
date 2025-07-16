# signalbot/signal_engine.py

from typing import List, Dict


class Signal:
    def __init__(self, token: str, direction: str, tp: List[float], sl: float, leverage: int, source: str, score: float):
        self.token = token.upper()
        self.direction = direction.lower()  # "long" or "short"
        self.tp = tp[:4]  # TP1–TP4
        self.sl = sl
        self.leverage = leverage
        self.source = source
        self.score = round(score, 3)

    def to_dict(self) -> Dict:
        return {
            "token": self.token,
            "direction": self.direction,
            "tp": self.tp,
            "sl": self.sl,
            "leverage": self.leverage,
            "source": self.source,
            "score": self.score,
        }

    def formatted(self) -> str:
        return (
            f"🆕 New Signal: {self.direction.upper()} {self.token}\n"
            f"🎯 TP1–TP4: {', '.join([str(t) for t in self.tp])}\n"
            f"🛑 SL: {self.sl} | Leverage: x{self.leverage}\n"
            f"📈 Signal Score: {self.score}\n"
            f"📡 Source: {self.source}"
        )
