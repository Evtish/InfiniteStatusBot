__all__ = (
    'random_time_delta',
    'get_time_to_type_text',
    'valid_chat',
    'send_reaction',
    'send_msg_with_typing'
)

import random, asyncio
from telethon.tl import functions, types
from config import client


def random_time_delta():
    return random.random() * random.randint(-1, 1)


def get_time_to_type_text(text: str) -> float:
    return text.count(' ') * 0.8 + random_time_delta()


async def valid_chat(chat) -> bool:
    return (
        not chat.bot and
        chat.id != (await client.get_me()).id
    )


async def send_reaction(event, sender, reaction: str) -> None:
    await asyncio.sleep(1.5 + 0.5 * random_time_delta())
    await client(functions.messages.SendReactionRequest(
        sender,
        event.id,
        add_to_recent=True,
        reaction=[types.ReactionEmoji(
            emoticon=reaction
        )]
    ))


async def send_msg_with_typing(event, text: str) -> None:
    async with client.action(event.chat_id, 'typing'):
        await asyncio.sleep(get_time_to_type_text(text))
        await event.reply(text)