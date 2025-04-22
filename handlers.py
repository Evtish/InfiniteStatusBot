__all__ = (
    # 'user_update_handler',
    'new_message_handler'
)

from telethon import events
from utils import *

# @events.register(events.UserUpdate)
# async def user_update_handler(event):
#     chat = await event.get_chat()

#     async def record_voice():
#         print('typing detected')
#         while event.typing:
#             print('still typing')
#             async with client.action(chat.id, 'record-audio'):
#                 await asyncio.sleep(1)
    
#     record_voice_task = asyncio.create_task(record_voice())

#     # await client.send_message(chat.id, 'чтото печатиш')
#     # await asyncio.sleep(10)
#     if event.typing and await valid_chat(chat):
#         await record_voice_task


@events.register(events.NewMessage(incoming=True))
async def new_message_handler(event):
    if event.message.text and 'чиназес' in event.message.text:# and random.random() <= 0.1:
        sender = await event.get_sender()
        reactions = ('👍', '❤️', '🙏')
        answer_text = 'ой брат правда такой чиназес чото'
        
        # await read_message(event, sender)        
        await send_reaction(event, sender, reactions)
        await send_msg_with_typing(event, answer_text)