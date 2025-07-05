import os
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()


def send_discord_alert(subject: str, sender: str):
    content = f"**New Important Email**\n**Subject**: {subject}\n**From**: {sender}"
    webhook = DiscordWebhook(url=os.getenv("DISCORD_WEBHOOK_URL"), content=content)
    response = webhook.execute()
    if response.status_code != 200:
        print("[ERROR] Failed to send Discord alert")
