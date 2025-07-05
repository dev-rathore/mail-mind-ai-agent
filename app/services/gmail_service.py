import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from typing import List, Dict
import os

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_gmail_service():
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    return build("gmail", "v1", credentials=creds)


def fetch_recent_emails(service, max_results=10) -> List[Dict]:
    result = service.users().messages().list(userId="me", maxResults=max_results).execute()
    messages = result.get("messages", [])

    emails = []
    for msg in messages:
        data = service.users().messages().get(userId="me", id=msg["id"], format="full").execute()
        headers = data["payload"]["headers"]
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown")

        parts = data["payload"].get("parts", [])
        body_data = ""
        if parts:
            for part in parts:
                if part["mimeType"] == "text/plain":
                    body_data = part["body"].get("data", "")
                    break
        else:
            body_data = data["payload"]["body"].get("data", "")

        try:
            body = base64.urlsafe_b64decode(body_data.encode("utf-8")).decode("utf-8")
        except Exception:
            body = "[Could not decode body]"

        emails.append({"subject": subject, "sender": sender, "body": body})

    return emails
