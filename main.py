import logging
from config import client, bot_token
from handlers import *

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    client.add_event_handler(user_update_handler)
    client.add_event_handler(new_message_handler)
    client.start()  # set the bot_token parameter equal to your bot_token if you want to use bot
    client.run_until_disconnected()