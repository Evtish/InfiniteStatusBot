__all__ = (
    'user_update_handler',
    'new_message_handler'
)

import asyncio
from telethon import events
import random
from config import client
from utils import *

event_data = {
    'tasks': {},
    'timers': {}
}


@events.register(events.UserUpdate)
async def user_update_handler(event):
    chat = await event.get_chat()
    if not await valid_chat(chat):
        return
    chat_id = chat.id

    async def animate_voice_recording():
        async with client.action(chat_id, 'record-audio'):
            await asyncio.sleep(3 + 2 * random_time_delta())
        await client.action(chat_id, 'cancel')

    if chat_id in event_data['tasks'] and not event_data['tasks'][chat_id].done():
        event_data['tasks'][chat_id].cancel()
        await client.action(chat_id, 'cancel')

    if event.typing:
        event_data['tasks'][chat_id] = asyncio.create_task(animate_voice_recording())


@events.register(events.NewMessage(incoming=True))
async def new_message_handler(event):
    chat_id = event.chat_id
    timeout = 10
    start_time = asyncio.get_event_loop().time()

    await asyncio.sleep(random.random())
    await client.send_read_acknowledge(
        entity=event.chat_id,
        message=event.id,
        max_id=event.id
    )
    
    print(start_time - event_data['timers'].get(chat_id, 0))
    if (
        event.text and
        'чиназес' in event.text and
        start_time - event_data['timers'].get(chat_id, 0) >= timeout
    ):
        event_data['timers'][chat_id] = start_time

        sender = await event.get_sender()
        reactions = ('👍', '❤️', '🙏')
        answer_texts = (
            'ой брат правда такой чиназес чото',
            'я смотрю у молодого чиназес лютый прям айай',
            'да конечно бро, вот так вот бамбамбам и чиназес сразу'
        )
        
        await send_reaction(event, sender, random.choice(reactions))
        await send_msg_with_typing(event, random.choice(answer_texts))