"""Telegram bot powered by OpenAI's responses.

This module wires a Telegram bot to relay user messages to an OpenAI
chat completion model and post the response back to the chat.
"""
from __future__ import annotations

import logging
import os
from typing import Optional

from openai import OpenAI
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_env_var(name: str) -> str:
    """Fetch ``name`` from the environment, raising a helpful error if missing."""
    value: Optional[str] = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Environment variable '{name}' must be set before running the bot."
        )
    return value


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Relay a plain-text Telegram message to OpenAI and reply with the response."""
    if update.message is None or update.message.text is None:
        logger.debug("Ignoring update without text: %s", update)
        return

    user_message = update.message.text
    chat_id = update.message.chat.id

    client = context.application.bot_data.get("openai_client")
    if client is None:
        raise RuntimeError("OpenAI client was not attached to bot_data.")

    logger.info("Forwarding message to OpenAI (chat_id=%s)", chat_id)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}],
    )

    reply_text = response.choices[0].message.content
    await context.bot.send_message(chat_id=chat_id, text=reply_text)


def build_application() -> "telegram.ext.Application":
    """Create the Telegram application with the configured handlers."""
    telegram_token = get_env_var("TELEGRAM_BOT_TOKEN")
    openai_api_key = get_env_var("OPENAI_API_KEY")

    application = ApplicationBuilder().token(telegram_token).build()
    application.bot_data["openai_client"] = OpenAI(api_key=openai_api_key)

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)
    return application


def main() -> None:
    """Entrypoint for running the Telegram bot."""
    app = build_application()
    logger.info("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
