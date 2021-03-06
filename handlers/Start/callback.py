from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_USERNAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME, OWNER_USERNAME
from handlers.play import cb_admin_check

@Client.on_callback_query(filters.regex("cbabout"))
async def cbabout(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>โ **About [๐๐ค๐ค๐ข๐ ๐๐๐ถ๐ฐ](https://t.me/{BOT_USERNAME})**</b> 

โ  **A powerfull bot for playing music for groups!

โ  Working with pyrogram

โ  Using Python 3.9.7

โ  Can play and download music or videos from YouTube

โ  I can make you happy

โ  For more info click /help

_๐๐ค๐ค๐ข-๐๐ฎ๐ฌ๐ข๐_licensed under the GNU General Public License v.3.0__

โข Updates channel @{UPDATES_CHANNEL}
โข Group Support @{GROUP_SUPPORT}
โข Assistant @{ASSISTANT_NAME}
โข Here is my [๐ข๐๐ป๐ฒ๐ฟ](t.me/godfatherakki)**

โ This Bot Belongs To DeCodee Team So Join For Quiry!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฆ๐๐ฝ๐ฝ๐ผ๐ฟ๐โโ", url="https://t.me/DeCodeSupport"
                    ),
                    InlineKeyboardButton(
                        "๐๐ต๐ฎ๐ป๐ป๐ฒ๐นโ", url="t.me/DeeCodeBots"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>โจ Welcome</b> {query.from_user.mention}!\n\n๐ญ [{BOT_NAME}](t.me/{UPDATES_CHANNEL}) <b>allows you to play music on groups through the new Telegram's voice chats!</b>\n\n๐ก <b>Find out</b> all the <b>Bot</b>'s <b>commands</b> and how they <b>work</b> by clicking on the ยป ๐ <b>Commands</b> button!""",
        reply_markup=InlineKeyboardMarkup(
             [ 
                [
                    InlineKeyboardButton(
                        "โ Add me to your Group โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "๐ Commands", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "โค๏ธ Donate", url=f"https://t.me/{OWNER_USERNAME}")
                ],[
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "โ๏ธ Info & About ๐จโ๐ป", callback_data="cbinfo")
                ],[
                    InlineKeyboardButton(
                        "๐งช Source Code ๐งช", url="https://GitHub.com/TeamDeeCoDe/DeCoDeMusic"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the basic commands</b>

๐ง [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytplay (song name) - play song directly from youtube 
/audio (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
/vk (song name) - download song from inline mode

๐ง [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/cache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
/rmd - remove all downloaded files
/clean - Remove all raw files""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

๐ note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ฎ here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Command List", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**๐ก here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โธ pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "โถ๏ธ resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฉ skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "โน end", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

๐ก **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

โ **usage:**

1๏ธโฃ ban & temporarily ban user from your group:
   ยป type `/b username/reply to message` ban permanently
   ยป type `/tb username/reply to message/duration` temporarily ban user
   ยป type `/ub username/reply to message` to unban user

2๏ธโฃ mute & temporarily mute user in your group:
   ยป type `/m username/reply to message` mute permanently
   ยป type `/tm username/reply to message/duration` temporarily mute user
   ยป type `/um username/reply to message` to unmute user

๐ note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Go Back", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**๐ก Feature:** delete every commands sent by users to avoid spam in groups !

โ usage:**

 1๏ธโฃ to turn on feature:
     ยป type `/delcmd on`
    
 2๏ธโฃ to turn off feature:
     ยป type `/delcmd off`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Go Back", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbinfo"
                    )
                ]
            ]
        )
    )

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**๐ฉโ๐ป INFORMATION** \n\n`๐ค This bot was created to listen Music in telegram group video chats.` \n\n`๐ก Powered by PyTgcalls the Async client API for the Telegram Group Calls.` \n\n**This bot licensed under GNU-GPL 3.0 License**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ How To Use Me", callback_data="cbhowtouse"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐งโ๐ปDevs", callback_data="cbdevs"
                    ),
                     InlineKeyboardButton(
                        "โ Commands", callback_data="cbcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbstart"
                    )
                ]
            ]
        )
    )

@Client.on_callback_query(filters.regex("cbdevs"))
async def cbdevs(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**CREDIT VC MUSIC PLAYER** \n\n`Here Some Developers Helping in Making The` **PRINCE MUSIC BOT**.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Eสสแดส", url=f"https://t.me/PROERRORXD"
                    ),
                     InlineKeyboardButton(
                        "Bสแดแดขแด", url=f"https://t.me/PIROXPOWER"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐๐ค๐ค๐ข(๐๐ฐ๐ง๐๐ซ) ", url=f"https://t.me/godfatherakki"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ก Back", callback_data="cbinfo"
                    )
                ]
            ]
        )
    )
