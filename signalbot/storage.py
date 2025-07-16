# signalbot/storage.py

import json
import os
from typing import List, Dict
from datetime import datetime

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def save_messages_to_json(messages: List[Dict], filename: str) -> str:
    """Save a list of messages to a JSON file inside /data."""
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(DATA_DIR, f"{filename}_{timestamp}.json")

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved {len(messages)} messages to {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Error saving messages to file: {e}")
        return ""
