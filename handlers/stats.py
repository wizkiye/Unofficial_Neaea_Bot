import datetime
import time

from pyrogram import Client, filters

from main import mongo, STARTED_TIME


@Client.on_message(
    filters.command("stats")
)
async def stats(_, message):
    users_count = await mongo.count_all(
        "USERS"
    )
    search_count = await mongo.count_all(
        "RESULTS"
    )
    up_time = str(datetime.timedelta(seconds=int(time.time()) - STARTED_TIME))
    await message.reply_text(
        f"**Stats**\n"
        f"**Active Users:** `{users_count}`\n"
        f"**Total Unique Searches:** `{search_count}`\n"
        f"**Uptime:** `{up_time}`"
    )
