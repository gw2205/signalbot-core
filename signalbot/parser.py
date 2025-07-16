# signalbot/parser.py

import re
from typing import Optional
from signalbot.signal_engine import Signal

def extract_signal(text: str, source: str = "unknown") -> Optional[Signal]:
    """
    Attempt to parse a trading signal from raw message text.
    Returns a Signal object if successful, otherwise None.
    """

    # Normalize text
    text = text.strip().lower()

    # Token (assumes 2–5 capital letters like BTC, ETH, PEPE)
    token_match = re.search(r"\b([A-Z]{2,5})\b", text.upper())
    token = token_match.group(1) if token_match else None

    # Direction
    if "long" in text:
        direction = "long"
    elif "short" in text:
        direction = "short"
    else:
        direction = None

    # Take Profits (TP1–TP4)
    tp_matches = re.findall(r"(tp[1-4]?)[^\d]{0,5}([\d\.]+)", text)
    tp_levels = sorted(list({float(val) for _, val in tp_matches}))[:4]

    # Stop Loss
    sl_match = re.search(r"sl[^\d]{0,5}([\d\.]+)", text)
    sl = float(sl_match.group(1)) if sl_match else None

    # Leverage (optional)
    lev_match = re.search(r"(\d{1,2})x", text)
    leverage = int(lev_match.group(1)) if lev_match else 25  # default

    # Score — set to 1.0 for now
    score = 1.0

    # Check if enough to return a signal
    if token and direction and sl and tp_levels:
        return Signal(
            token=token,
            direction=direction,
            tp=tp_levels,
            sl=sl,
            leverage=leverage,
            source=source,
            score=score,
        )

    return None
