import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_signal_to_telegram(group: str, message: str, confidence: float):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials missing. Check your .env file.")
        return

    text = f"📢 New Signal from *{group}*\n\n💬 {message}\n📊 Confidence: *{confidence:.2f}*"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ Signal sent to Telegram.")
    else:
        print(f"❌ Failed to send Telegram message: {response.text}")
