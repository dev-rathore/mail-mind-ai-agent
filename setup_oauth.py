# Run this script once to generate token.json from credentials.json

import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

CREDENTIALS_PATH = Path("credentials.json")
TOKEN_PATH = Path("token.json")


def run_oauth_flow():
    if not CREDENTIALS_PATH.exists():
        print("[ERROR] Missing credentials.json file in project root.")
        print("Visit https://console.cloud.google.com/ to download your credentials.")
        sys.exit(1)

    print("Starting OAuth flow for Gmail API...")

    flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_PATH), SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(TOKEN_PATH, "w") as token:
        token.write(creds.to_json())

    print("\ntoken.json has been generated!")
    print("You're now authenticated and can run the agent.")


if __name__ == "__main__":
    run_oauth_flow()
