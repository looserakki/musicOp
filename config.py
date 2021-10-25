import os
from os import getenv

que = {}
admins = {}
API_ID = int(getenv("API_ID", "6285038"))
API_HASH = getenv("API_HASH", "cea8174655dfd00fb51f91f8493e55ee")
BOT_TOKEN = getenv("BOT_TOKEN", "1795262909:AAEo-lLCMFKvTBpJByuVC_AVuu-kq5epoeY")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
THUMB_IMG = getenv("THUMB_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
AUD_IMG = getenv("AUD_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
QUE_IMG = getenv("QUE_IMG", "https://te.legra.ph/file/1b5f32e7b440302ac6435.png")
BOT_USERNAME = getenv("BOT_USERNAME", "DeCodeMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "akki-assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DeCodeSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DeecodeBots")
OWNER_NAME = getenv("OWNER_NAME", "Akki") # isi dengan name kamu tanpa simbol @
OWNER_USERNAME = getenv("OWNER_USERNAME", "godfatherakki") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID", "2007701745")) # fill with your id as the owner of the bot
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Anmol:ix7ol6TyciICTigD@cluster0.nu8bu.mongodb.net/Anmol?retryWrites=true&w=majority") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001173097859")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2007701745 936481432").split()))
SESSION_NAME = getenv("SESSION_NAME", "BQAHq60EG5uZhhNlYUUm1OPfE3bdmNhFndZhJ9r-KTZCvjnhPY53gTAlBlFomgTCD0uYyhoA1xCYRP8Gik7u8nf7uLSngws_xbDrkjUEPLl9rgklhFuMJtCIJ9grrMBzi0LaV9v9TnhURCfy6pOqNiVXAiDzSI_hWlTqb4gNkPrMEAcRcQ8cQr1gMG2gekkJ4HyOVqxVgb6QalYDWy19ao7ipllbBsazb61B5EBQy3JIbfOBpJy1_DhygBm2aKRmRG38V2eRHj-I1fQO3QnF2H4TYYgS9ZM0m5l-IfTYWlXvnTVBuOzStLmL3Cx7B_wjxbaE6Y3uLSFNzo84UdiTzMV_fC2BLwA")
BOT_NAME = getenv("BOT_NAME", "𝐀𝐤𝐤𝐢 𝐌𝐮𝐬𝐢𝐜")
