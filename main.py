# main.py

import asyncio
from signalbot.collector import fetch_group_messages
from signalbot.parser import extract_signal
from signalbot.signal_executor import send_signal_to_telegram
from signalbot.storage import save_messages_to_json

async def run(group: str):
    print(f"📡 Scanning group: {group}")
    messages = await fetch_group_messages(group_username=group, limit=25)

    if not messages:
        print("❌ No messages found.")
        return

    # Save raw messages
    save_messages_to_json(messages, filename=group)

    for msg in messages:
        signal = extract_signal(msg["text"], source=group)
        if signal:
            print("✅ Parsed signal:")
            print(signal.formatted())
            sent = send_signal_to_telegram(signal.formatted())
            if sent:
                print("🚀 Signal sent to Telegram!")
            else:
                print("⚠️ Failed to send to Telegram.")
        else:
            print("➖ No valid signal found in message.")

if __name__ == "__main__":
    asyncio.run(run("USABitcoinArmy"))
