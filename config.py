import os
from os import getenv

que = {}

SESSION_NAME = getenv("SESSION_NAME", "BQByiKO0jlcrY4nNDRgjJkbUrgGAi25N4qCz4Sf9qfcaAaYoTKBfvxSex1QZ2z9zAvssdj8Mm5bI-hJczVWAcZFBocZoGbuuIOPhZsKZSiE7mMbnl-RgTWZJe3PbDOgDWL-Uvkpxy11fx_gNVWwVotu4t4X_BxGt9qPy0GG13O_JwHNpDzvwr-qMhbqLcLH4SY3BPcjyE-peaDg70V7Ban6VwzFSNCens59jx3diNhE2ModF-SH3ih0f7kPTima6yKFkiyo3GUl056_T8z8XhYpto-5CQVlXBoLqUeZLSlaIuKT7WODtq4dQ0FcXbxKKhMo2siPqFRjf2hRZt1meH4DrfC2BLwA")
BOT_TOKEN = getenv("BOT_TOKEN", "1795262909:AAHyTXPuRnSwTJzqfVWewN70l6gTSelUOYQ")
BOT_NAME = getenv("BOT_NAME", "𝐀𝐤𝐤𝐢 𝐌𝐮𝐬𝐢𝐜")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "AKKI-ASSISTANT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DeeCodeBots")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GodfatherSupport")
BOT_USERNAME = getenv("BOT_USERNAME", "AKKIMUSIC_BOT")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
THUMB_IMG = getenv("THUMB_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
AUD_IMG = getenv("AUD_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
QUE_IMG = getenv("QUE_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")

admins = {}
API_ID = int(getenv("API_ID", "6285038"))
API_HASH = getenv("API_HASH", "cea8174655dfd00fb51f91f8493e55ee")

OWNER_ID = int(getenv("OWNER_ID", "2007701745"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "400"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2007701745 936481432").split()))

ASSISTANT_NAME = getenv("ASSISTANT_NAME", "akki-assistant")
OWNER_NAME = getenv("OWNER_NAME", "Akki") # isi dengan name kamu tanpa simbol @
OWNER_USERNAME = getenv("OWNER_USERNAME", "godfatherakki") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Anmol:ix7ol6TyciICTigD@cluster0.nu8bu.mongodb.net/Anmol?retryWrites=true&w=majority") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001173097859")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
