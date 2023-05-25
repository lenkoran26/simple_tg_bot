import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_TOKEN = os.environ.get("TOKEN")
BOT_TOKEN = os.environ.get("NEW_TOKEN")