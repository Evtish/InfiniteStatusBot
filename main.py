import logging
from config import client, bot_token
from handlers import *


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    client.add_event_handler(user_update_handler)
    client.add_event_handler(new_message_handler)
    client.start()  # set the bot_token parameter equal to your bot_token if you want to use bot
    client.run_until_disconnected()


if __name__ == '__main__':
    main()