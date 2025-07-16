# SignalBot Core

SignalBot Core is a minimalist crypto signal engine designed for high-leverage scalping (x25/x50).  
It scans live market sentiment from Telegram, YouTube, and other data sources, validates signal strength using volatility filters, and pushes real-time alerts to your Telegram bot.

---
## ⚙️ Core Features

- ✅ Sentiment score calculation using keyword engine  
- ✅ Signal structure support for Telegram/YouTube/Reddit posts  
- ✅ VolatilityGuard: Filters based on token price volatility  
- ✅ Scalp-friendly TP/SL system with confidence scoring  
- ✅ FastAPI endpoint (`main.py`) for live monitoring and API  
- ✅ Telegram bot integration for automated push  

---

## 📁 Project Structure

signalbot-core/
│
├── kaizennew/
│ ├── sentibot/ # Keyword-based sentiment analysis engine
│ ├── signalbot/ # Signal evaluator and executor
│ ├── guard/ # Volatility + macro trend filters
│ └── mexc/ # Live token price fetcher (via MEXC API)
│
├── data/ # Curated source lists (YouTube, Telegram, etc.)
├── main.py # FastAPI server to run the SignalBot
├── test_imports.py # QA script to validate all module imports
---

## ⚡ Quick Start

Clone the repo and run with FastAPI and Uvicorn:

```bash
git clone https://github.com/YOUR_USERNAME/signalbot-core.git
cd signalbot-core
PYTHONPATH=. python3 -m uvicorn main:app --reload
🚨 New Signal: PEPEUSDT
🟢 Long Signal | Sentiment Score: 0.91
🎯 TP1–TP4: 0.000033, 0.000036, 0.000039, 0.000041
🛑 SL: 0.000028 | Leverage: x25
Source: @USABitcoinArmy
---

## 📜 License

MIT License  
Created and maintained by **Gai Winter**
