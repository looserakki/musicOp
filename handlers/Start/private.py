import shutil
import psutil
from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only
from helpers.decorators import humanbytes
from helpers.database import db
from handlers import __version__

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>โจ **๐๐ก๐๐ฅ๐๐จ๐ฆ๐ {message.from_user.first_name}** \n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ๐ฎ๐น๐น๐ผ๐ ๐๐ผ๐ ๐๐ผ ๐ฝ๐น๐ฎ๐ ๐บ๐๐๐ถ๐ฐ ๐ผ๐ป ๐ด๐ฟ๐ผ๐๐ฝ๐ ๐๐ต๐ฟ๐ผ๐๐ด๐ต ๐๐ต๐ฒ ๐ป๐ฒ๐ ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ'๐ ๐๐ผ๐ถ๐ฐ๐ฒ ๐ฐ๐ต๐ฎ๐๐ ๐ฉ๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ ๐๐๐๐จ๐๐!**

๐ก **๐๐ถ๐ป๐ฑ ๐ผ๐๐ ๐ฎ๐น๐น ๐๐ต๐ฒ ๐๐ผ๐'๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฎ๐ป๐ฑ ๐ต๐ผ๐ ๐๐ต๐ฒ๐ ๐๐ผ๐ฟ๐ธ ๐ฏ๐ ๐ฐ๐น๐ถ๐ฐ๐ธ๐ถ๐ป๐ด ๐ผ๐ป ๐๐ต๐ฒ ยป ๐ ๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฏ๐๐๐๐ผ๐ป !**

โ **๐๐ผ๐ฟ ๐ถ๐ป๐ณ๐ผ๐ฟ๐บ๐ฎ๐๐ถ๐ผ๐ป ๐ฎ๐ฏ๐ผ๐๐ ๐ฎ๐น๐น ๐ณ๐ฒ๐ฎ๐๐๐ฟ๐ฒ ๐ผ๐ณ ๐๐ต๐ถ๐ ๐ฏ๐ผ๐, ๐ท๐๐๐ ๐๐๐ฝ๐ฒ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "โ Aแดแด Mแด Tแด Uส Cสแดแด๊ฑ ๐", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "๐ข Hแดแดก Tแด U๊ฑแด Mแด", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "๐ Cแดแดแดแดษดแด๊ฑ", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "๐ Dแดแด?แดสแดแดแดส", url=f"https://t.me/DeeCodeDevs")
                ],[
                    InlineKeyboardButton(
                        "๐ฅ O๊ฐ๊ฐษชแดษชแดส Sแดแดแดแดสแด", url=f"https://t.me/DeCodeSupport"
                    ),
                    InlineKeyboardButton(
                        "๐ฅ O๊ฐ๊ฐษชแดษชแดส Cสแดษดษดแดส", url=f"https://t.me/DeeCodeBots")
                ],[
                    InlineKeyboardButton(
                        "๐ O๊ฐ๊ฐษชแดษชแดส Cสแดแด", url="https://t.me/hindi_shayri_story")
                ],[
                    InlineKeyboardButton(
                        "๐ Sแดแดสแดแด Cแดแดแด", url="https://github.com/TeamDeeCode/DeCoDeMusic"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""โ **Bแดแด I๊ฑ Rแดษดษดษชษดษข**\n<b>๐? **Uแดแดษชแดแด:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โจ Gสแดแดแด", url=f"https://t.me/DeCodeSupport"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Cสแดษดษดแดส", url=f"https://t.me/DeeCodeBots"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐๐ป **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands powered By DeCode!**

โก __Powered by {BOT_NAME} Dแดแดแดแดแด""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="โ Hแดแดก Tแด U๊ฑแด Mแด", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐ก Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

โก __Powered by {BOT_NAME} Dแดแดแดแดแด__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โก Bแด๊ฑษชแด Cแดแด๊ฑ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "โฃ๏ธ Aแดแด?แดษดแดแดแด Cแดแด๊ฑ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Aแดแดษชษด Cแดแด๊ฑ", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "โฒ๏ธ Sแดแดแด Cแดแด๊ฑ", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Oแดกษดแดส Cแดแด๊ฑ", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fแดษด Cแดแด๊ฑ", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def ping_pong(client: Client, message: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    delta_ping = time() - start
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bba35e8f0a81cb9203d7b.jpg", 
        caption=f"๐ ๐ฃ๐ข๐ก๐!!\n"
                  f"โก** {delta_ping * 1000:.3f} **  ๐?๐\n\n** ๐๐๐๐๐๐ โ๏ธ **\n\n**Uแดแดษชแดแด:** {uptime}\n\n** ๐ฆ๐ง๐๐ง๐๐ฆ๐ง๐๐๐ฆ ๐ ** \n\n**๐ค bot version:** `{__version__}` \n\n**๐๐ผ total users:** \n ยป **on bot pm:** `{total_users}` \n\n**๐พ disk usage:** \n\nยป **disk space:** `{total}` \n ยป **used:** `{used}({disk_usage}%)` \n ยป **free:** `{free}` \n\n**๐ hardware usage:** \n\n ยป **CPU usage:** `{cpu_usage}%` \n ยป **RAM usage:** `{ram_usage}%`",      
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "แดสแดแดแด", callback_data="cbabout"
                     ),
                     InlineKeyboardButton(
                         "แดสแดษดษดแดส", url=f"https://t.me/DeecodeBots"
                     )
                 ]
             ]
         )
     )

@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐ค Sแดแดแดแด๊ฑ:\n"
        f"โข **Uแดแดษชแดแด:** `{uptime}`\n"
        f"โข **Sแดแดสแด Tษชแดแด:** `{START_TIME_ISO}`"
    )
