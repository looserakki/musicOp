from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Give rights to your Group and try again</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "DeCoDeMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I joined here at your command")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Userbot Already In Your Chat</b>",
        ) 
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑Error waiting for flood decay 🛑  \n  Participant {user.first_name} could not join your group due to a large number of requests to join the user bot! Check the blacklist, unban the bot user if it is there. "
            "\ n \ nOr manually add Assistant to your Group and try again </b>",
        )
        return
    await message.reply_text(
            "<b>an assistant has joined your chat</b>",
        )
    
