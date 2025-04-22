__all__ = (
    'get_time_to_type_text',
    'valid_chat',
    'read_message',
    'send_reaction',
    'send_msg_with_typing'
)

import random, asyncio
from telethon.tl import functions, types
from config import client
from typing import Iterable


def get_time_to_type_text(text: str) -> float:
    return text.count(' ') * 0.8 + random.random() * random.randint(-1, 1)


async def valid_chat(chat) -> bool:
    return (
        not chat.bot and
        chat.id != (await client.get_me()).id
    )


async def read_message(event, sender) -> None:
    await client(functions.messages.ReadDiscussionRequest(
        sender,
        event.id,
        event.id
    ))


async def send_reaction(event, sender, reactions: Iterable) -> None:
    await asyncio.sleep(1.5)
    await client(functions.messages.SendReactionRequest(
        sender,
        event.id,
        add_to_recent=True,
        reaction=[types.ReactionEmoji(
            emoticon=random.choice(reactions)
        )]
    ))


async def send_msg_with_typing(event, text: str) -> None:
    async with client.action(event.chat_id, 'typing'):
        await asyncio.sleep(get_time_to_type_text(text))
        await event.reply(text)
    # await asyncio.sleep(60)