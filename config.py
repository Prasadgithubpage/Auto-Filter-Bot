import os
import logging
from logging.handlers import RotatingFileHandler

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

# Shorten the log file name
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
