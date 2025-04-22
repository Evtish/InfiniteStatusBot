import logging, handlers
from config import client
# from handlers import *

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    # client.add_event_handler(handlers.user_update_handler)
    client.add_event_handler(handlers.new_message_handler)
    client.start()
    client.run_until_disconnected()