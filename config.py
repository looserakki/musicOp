import os
from os import getenv

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCwn_AGNAFth8xxQeicoMMkltILzx8Kxtin_C-e4spjlEZA7Z0xh8Z7xab94C_w3IWWgLkvHttpJMfTCov_1ZE4Nj3uJPVOE2g96PrYnsqgGIwY3dThsc5gMI1hWDywUJMZJB-WcPPD4gc9cguytxJvigL28Si1guy5_VvaH9nN5n7ns4_CtnO_krGVctO9E8FkgRucj9zuID7y-EwD6YVkB9cfIvuvf1qRl4TtkOETncoHQrHHrIMoEAgJgWyq7vq-BpDzxSvdlc2s5vxAYYEjebnYKe6Tyq3W2EOOU9OYTqBjNOsF3AYgWVYRTodKzOau7t389zPfcr-sUk8BxNKNdN7njwA")
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
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Xd_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DeCodeSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DeecodeBots")
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
SESSION_NAME1= getenv("SESSION_NAME1", "AQCuN_CjNcxTMO4_Gts3NcNgM-vCkSSPXIRWugRrKZpANVfW33dCkAKBvTuTnJc8sHiEFFRBYmr9ExIOV3gVHqRRSJAQU94QLItYz_aVBmO23PgKXma26qznJYl4orzKMZjL5a-3m0TJHeBQ_midf4LKzpPLZrfrzBkLXVJXPGDsa7dymWkNbNPh9WWsU2L2g4VncxY-njoHz5kGErKXc0px-2BLSePd14eyABjeeudd9Q8QC0S7LQcQWMGC-Rp9WpXLqVRBEp0Qq3i9pj-bZ7NrXKMIi68mUTnnrF8t_jo0WEClZm3yCVEkmX_v2ninoS_REg8hizTKmOJzjup2dB-seLPLNgA") 
API_ID1= getenv("API_ID1", "6435225") 
API_HASH1= getenv("API_HASH1", "4e984ea35f854762dcde906dce426c2d") 
