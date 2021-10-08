import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQDBu9FvVlc6lJpXXom1Um8heUCMDvnXWRWW6-ZrEQaJxKvpwFY4bEuvVlxwuZQUQeNLN68Gh3QyeiaNm7CAuVleXMp5KRSlXwILv-nGDd2h5xqVDN_n_-siqBCvpE47jbj9iSYJXfHugsUSUanmnFVVLJ4kOydSBhIH_zbjyw3sKeaovZnk5QnqOW07UdaBSMdJYH2_rSS6ojQ_gbYkkqq7BarlVuZPcmciNlRTLuALFkHJtLdlRGOp3hVszxFeZ0HY3pyPEC8UZ9SPkOzrVjwCDg6CFHdOZzg6e72spqgkmLPV8BX9lGW4mO1iPpMqsokNu3nMvKhLfESo5r59IRwKdN7njwA")
BOT_TOKEN = getenv("BOT_TOKEN", "2020813025:AAHvDTniAFZSnL1VWM3Z58Jp8W7Q7JSHl6w")
BOT_NAME = getenv("BOT_NAME", "DeCodeMusic")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
THUMB_IMG = getenv("THUMB_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
AUD_IMG = getenv("AUD_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
QUE_IMG = getenv("QUE_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
API_ID = int(getenv("API_ID", "8636372"))
API_HASH = getenv("API_HASH", "7dd38153ba6f48bfd990a8067e5b8498")
BOT_USERNAME = getenv("BOT_USERNAME", "DeCodeMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DeCodeMusic_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DeCodeSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DecodeBots")
OWNER_NAME = getenv("OWNER_NAME", "Blaze_Op") # isi dengan name kamu tanpa simbol @
OWNER_USERNAME = getenv("OWNER_USERNAME", "piroXpower") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID", "2007701745")) # fill with your id as the owner of the bot
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Anmol:ix7ol6TyciICTigD@cluster0.nu8bu.mongodb.net/Anmol?retryWrites=true&w=majority") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001173097859")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2007701745").split()))
