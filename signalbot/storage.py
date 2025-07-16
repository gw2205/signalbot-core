import os
import json
from datetime import datetime

DATA_DIR = "data"

# Ensure the data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_messages_to_json(group_name, messages):
    """
    Save messages from a group to a JSON file with timestamped entries.
    """
    filename = os.path.join(DATA_DIR, f"{group_name}_messages.json")
    
    timestamped_messages = []
    for message in messages:
        timestamped_messages.append({
            "timestamp": datetime.utcnow().isoformat(),
            "text": message
        })

    # Append to file if exists, otherwise create
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            existing = json.load(f)
        existing.extend(timestamped_messages)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2)
    else:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(timestamped_messages, f, indent=2)
