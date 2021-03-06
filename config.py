import os

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URI = os.getenv('MONGO_DB_URI')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
PROXY = os.getenv("PROXY")
ADMIN = os.getenv("ADMIN")
BOT_USERNAME = os.getenv("BOT_USERNAME")