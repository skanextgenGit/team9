# Telegram Bot with OpenAI Integration

This project contains a small Telegram bot that forwards incoming messages to an OpenAI Chat Completions model and responds with the generated reply.

## Prerequisites
- Python 3.10+
- A Telegram bot token
- An OpenAI API key

## Quickstart
1. **Clone and enter the project directory** (skip if you're already here):
   ```bash
   git clone <your-fork-or-clone-url>
   cd team9
   ```
2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   On Windows PowerShell, activate it with:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
3. **Install the Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Set the required environment variables before launching the bot:

```bash
export TELEGRAM_BOT_TOKEN="<your-telegram-bot-token>"
export OPENAI_API_KEY="<your-openai-api-key>"
```

You can store these values in an `.env` file or use another secret-management approach if preferred.

## Running the Bot
Start the bot with:

```bash
python bot.py
```

The bot will begin polling Telegram for new messages and respond with OpenAI-generated replies. Check the console logs for status updates.

If you prefer, you can keep your environment variables in a `.env` file and load them before running the script:

```bash
export $(grep -v '^#' .env | xargs)
python bot.py
```

Replace `.env` with the path to the file that stores your secrets.

## Troubleshooting
- Ensure the environment variables are set in the same shell session where you run `python bot.py`.
- Confirm that the bot token has access to the chat where you are sending messages.
- If you see import errors, verify that the dependencies installed correctly.

## License
This project is provided as-is without a specific license.
