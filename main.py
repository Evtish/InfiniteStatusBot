import logging
from config import client, bot_token
from handlers import *

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    client.add_event_handler(user_update_handler)
    # client.add_event_handler(new_message_handler)
    client.start(bot_token=bot_token)
    client.run_until_disconnected()