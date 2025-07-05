import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

NOTION_API_URL = "https://api.notion.com/v1/pages"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('NOTION_API_KEY')}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


def save_to_notion(subject: str, sender: str, body: str):
    now = datetime.now().isoformat()
    payload = {
        "parent": {"database_id": os.getenv("NOTION_DATABASE_ID")},
        "properties": {
            "Date": {"date": {"start": now}},
            "Subject": {"title": [{"text": {"content": subject}}]},
            "Sender": {"rich_text": [{"text": {"content": sender}}]},
            "Body": {"rich_text": [{"text": {"content": body[:1000]}}]},
        },
    }
    resp = requests.post(NOTION_API_URL, headers=HEADERS, json=payload)
    if not resp.ok:
        print("[ERROR] Failed to save to Notion:", resp.text)
