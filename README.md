# Mail Mind AI Agent

Automatically classify Gmail emails using Google's Gemini AI. If an email is important, it:

- Stores it to a Notion database in a structured table format
- Sends a notification to a Discord channel

---

## Features

- Gmail API integration to fetch recent emails
- Gemini AI (Google Generative AI) for classifying importance
- Notion API integration for structured storage
- Discord Webhook alert system
- Cron-based GitHub Actions automation
- `Makefile`, `Dockerfile`, and `pyproject.toml` included

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/dev-rathore/mail-mind-ai-agent.git
cd mail-mind-ai-agent
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv .venv # or python -m venv .venv on Windows
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies with `uv`

```bash
pip install uv  # if not already installed
make install    # runs: uv pip install -e .
```

### 4. Setup `.env`

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
NOTION_API_KEY=your_notion_api_key
NOTION_DATABASE_ID=your_notion_db_id
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

### 5. Authenticate with Gmail

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable **Gmail API**
- Create OAuth client credentials and download `credentials.json`
- Authenticate:

```bash
python setup_oauth.py
```

- Save the token as `token.json`

---

## Usage

### Run the agent manually

```bash
make run
```

### Or run via CLI shortcut

```bash
mail-mind-ai-agent
```

### Format and lint your code

```bash
make format
make lint
```

---

## Docker Support

### Build the image

```bash
make docker-build
```

### Run the container

```bash
make docker-run
```

---

## GitHub Actions

This project includes a workflow (`.github/workflows/mail_mind_ai_agent.yml`) that:

- Runs daily at 8 AM UTC
- Or can be triggered manually

> Make sure to add these GitHub secrets:
>
> - `GEMINI_API_KEY`
> - `NOTION_API_KEY`
> - `NOTION_DATABASE_ID`
> - `DISCORD_WEBHOOK_URL`

---

## License

MIT. Free to use with attribution.
