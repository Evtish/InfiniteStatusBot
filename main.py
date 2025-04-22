import logging, asyncio, random
from telethon import events
from config import client

logging.basicConfig(
    # format='[%(levelname) %(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)


async def valid_chat(chat):
    return (
        not chat.bot and
        chat.id != (await client.get_me()).id
    )


# async def main():
#     async with client.action(1644081190, 'record-audio'):
#         await asyncio.sleep(10)


@client.on(events.UserUpdate)
async def user_update_handler(event):
    chat = await event.get_chat()
    # print(chat)
    # print(event.chat_id, event.sender_id)
    if event.typing and await valid_chat(chat):
        print('typing detected')
        # await client.send_message(chat.id, 'чтото печатиш')
        # await asyncio.sleep(10)
        async with client.action(chat.id, 'record-audio'):
            await asyncio.sleep(5)


@client.on(events.NewMessage(incoming=True, pattern='чиназес'))
async def new_message_handler(event):
    answer_text = 'ай брат ай молодой'
    # print((await client.get_me()).id == (await event.get_sender()).id)
    async with client.action(event.sender_id, 'typing'):
        await asyncio.sleep(answer_text.count(' ') + random.random() * random.randint(-1, 1))
        await client.send_message(event.sender_id, answer_text)
    # await asyncio.sleep(60)


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()