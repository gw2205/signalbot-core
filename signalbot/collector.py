# signalbot/collector.py

import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel

load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

client = TelegramClient("signalbot_session", API_ID, API_HASH)

async def fetch_group_messages(group_username: str, limit: int = 10):
    await client.start()
    messages = []
    try:
        async for message in client.iter_messages(group_username, limit=limit):
            messages.append({
                "text": message.text,
                "date": str(message.date),
                "id": message.id,
                "sender_id": getattr(message.sender_id, 'user_id', None),
            })
    except Exception as e:
        print(f"❌ Error fetching messages: {e}")
    finally:
        await client.disconnect()
    return messages

if __name__ == "__main__":
    import asyncio

    # Replace with any public group or channel username (e.g., 'USABitcoinArmy')
    group = "USABitcoinArmy"
    fetched = asyncio.run(fetch_group_messages(group))
    
    print(f"✅ Pulled {len(fetched)} messages from @{group}")
    for msg in fetched:
        print(f"📨 {msg['date']} | {msg['text'][:100]}")
