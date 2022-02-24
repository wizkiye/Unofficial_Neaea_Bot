from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("info"))
async def info(_, message: Message):
    await message.reply_text(
        "**Unofficial Neaea Telegram Bot**\n"
        "**Created by**: [By this dude](https://github.com/wizkiye)\n"
        "**Source code**: [here](https://github.com/wizkiye/neaea_scraper_bot)\n"
        "`Don't forget to star the repo if you like it!`\n"
        "**Bot version**: __1.0.0__\n"
        "**Secret link**: [https://neaeahacked.com](https://m.youtube.com/watch?v=dQw4w9WgXcQ)\n",
        disable_web_page_preview=False,
        parse_mode="markdown"
    )
