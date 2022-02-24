from neaea import Neaea
from pyrogram import Client

import config
from database import AsyncMongo

mongo = AsyncMongo(config.MONGO_DB_URI, "NEAEA")
neaea = Neaea(
    mongo=mongo,
)
bot = Client(
    ":memory:",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    plugins=dict(root="handlers"),
    bot_token=config.BOT_TOKEN,
)

if __name__ == "__main__":
    print("Starting bot...")
    bot.run()
