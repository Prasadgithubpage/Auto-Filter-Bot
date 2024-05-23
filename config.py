
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "")

# Generate a user session string 
TG_USER_SESSION = ("BQF3TIEAqUI8tHMPvkABoOCULrzSyTcLKGl13sEqa89wdQbAoCiU7a-ZsGtMLgAGku0z-y5B32eVqFewhsGfx3DH0jHiRJk9mAtzqz_2xGtvoeHScPf-HCJNPHHYHJSBgsVXCfwKY_YaSHkmCIV_9SDaCyNpXVbSR931yTKRUDtnASM9HKwNR_apMrBbejc209-MJS6IOwPmTt7oaAqhLxYl63ITvUmE3MrK1mJX4mjxOgKGGCi2XOi_DJjZV2pEGrwwhhyIpvxVfmYA11T8RQX59rLiNvYtHlZjEZ3MqBBGjTINwrFTJ8zVDJ-yGqEijGY6aEplOgl_S_A_ji4gab25uClwAAAAAAFE3SXbAA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

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
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
