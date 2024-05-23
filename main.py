#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

import os
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script

# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "")

# ID of Channel from which the bot should search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "")

TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

# Set the logging level for the Pyrogram library to WARNING
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Define a LOGGER function to get a logger object with the specified name
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


# Create Pyrogram Client
app = Client(
    TG_BOT_SESSION,
    api_hash=API_HASH,
    api_id=APP_ID,
    plugins=dict(root="plugins"),
    workers=TG_BOT_WORKERS,
    bot_token=TG_BOT_TOKEN
)

# Button data
BUTTONS = {}


# Command handlers
@app.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("HELP", callback_data="help_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⭕️ JOIN OUR CHANNEL ⭕️", url="https://t.me/TroJanzHEX")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except Exception as e:
        LOGGER(__name__).error(f"An error occurred in start command handler: {e}")


@app.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="start_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⭕️ SUPPORT ⭕️", url="https://t.me/TroJanzSupport")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except Exception as e:
        LOGGER(__name__).error(f"An error occurred in help command handler: {e}")


@app.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="help_data"),
                        InlineKeyboardButton("START", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE", url="https://github.com/TroJanzHEX/Auto-Filter-Bot")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except Exception as e:
        LOGGER(__name__).error(f"An error occurred in about command handler: {e}")


@app.on_callback_query()
async def cb_handler(client, query):
    try:
        # Add your callback query handler logic here
        pass
    except Exception as e:
        LOGGER(__name__).error(f"An error occurred in callback query handler: {e}")


def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == "__main__":
    app.run()
