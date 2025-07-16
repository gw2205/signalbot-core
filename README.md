# SignalBot Core

SignalBot Core is a real-time sentiment analysis and signal execution engine for crypto trading.  
It scans Telegram groups, YouTube traders, and other sentiment sources to identify high-probability setups based on NLP scoring, market volatility, and live MEXC data.

## Features
- 🔍 Sentiment scoring based on keywords
- 📊 Volatility filtering with custom thresholds
- 🧠 Strategy execution engine (TP/SL, trail stops, learning)
- 📡 Signal validation and Telegram push
- 🧪 Fully testable and modular

## Project Structure
- `sentibot/` – Sentiment analysis engine
- `signalbot/` – Signal scoring and execution logic
- `guard/` – Macro trend and volatility monitors
- `data/` – All real source files (Telegram, YouTube, keywords, etc.)
- `main.py` – FastAPI app entrypoint

---

🚀 Built for high-leverage crypto scalping (x25/x50) with real data  
👤 Developed by a private crypto trader
