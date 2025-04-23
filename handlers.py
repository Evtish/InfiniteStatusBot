__all__ = (
    'user_update_handler',
    # 'new_message_handler'
)

import asyncio
from telethon import events
from config import client
from utils import *

typing_status = {}


@events.register(events.NewMessage(incoming=True))
async def user_update_handler(event):
    chat = await event.get_chat()
    if not await valid_chat(chat):
        return
    chat_id = chat.id

    async def animate_voice_recording():
        async with client.action(chat_id, 'record-audio'):
            await asyncio.sleep(5)
        await client.action(chat_id, 'cancel')
        typing_status.pop(chat_id, None)

    if chat_id in typing_status and not typing_status[chat_id].done():
        typing_status[chat_id].cancel()
        await client.action(chat_id, 'cancel')
        typing_status.pop(chat_id, None)

    if event.text and 'hi' in event.text:
        typing_status[chat_id] = asyncio.create_task(animate_voice_recording())


# @events.register(events.NewMessage(incoming=True))
# async def new_message_handler(event):
#     if event.message.text and 'чиназес' in event.message.text:# and random.random() <= 0.1:
#         sender = await event.get_sender()
#         reactions = ('👍', '❤️', '🙏')
#         answer_text = 'ой брат правда такой чиназес чото'
        
#         # await read_message(event, sender)        
#         await send_reaction(event, sender, reactions)
#         await send_msg_with_typing(event, answer_text)