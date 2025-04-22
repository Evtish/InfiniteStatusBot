from telethon import TelegramClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()  # create .env file and put your api_id and api_hash into corresponing variables

api_id = getenv('api_id')
api_hash = getenv('api_hash')
client = TelegramClient('main', api_id, api_hash)  # your session file must be called main.session