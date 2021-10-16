from pyrogram import Client
from pytgcalls import PyTgCalls
from pyrogram import idle

import config
from . import queues

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
client1 = Client(config.SESSION_NAME1, config.API_ID1, config.API_HASH1)

pytgcalls = PyTgCalls(client)
pytgcalls1 = PyTgCalls(client1)



@pytgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(
            chat_id, queues.get(chat_id)["file"]
        )


run = pytgcalls.run

run = pytgcalls1.run
idle() 
