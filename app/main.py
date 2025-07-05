from services.gmail_service import get_gmail_service, fetch_recent_emails
from services.notion_service import save_to_notion
from services.discord_service import send_discord_alert
from agents.gemini_agent import is_email_important

def run_agent():
    service = get_gmail_service()
    print("Fetching emails...")
    emails = fetch_recent_emails(service)

    for email in emails:
        print(f"Checking: {email['subject']}")
        if is_email_important(email["subject"], email["body"]):
            print("-> Important. Logging to Notion and notifying Discord.")
            save_to_notion(email["subject"], email["sender"], email["body"])
            send_discord_alert(email["subject"], email["sender"])
        else:
            print("-> Not important.")


if __name__ == "__main__":
    run_agent()
