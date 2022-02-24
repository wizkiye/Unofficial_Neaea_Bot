from pyrogram import Client, filters


@Client.on_message(
    filters.command(['help'])
)
async def help_(_, message):
    await message.reply_text(
        text="""
        You can see your result by sending your registration number.\n\n
Use        /start - to restart the bot
Use        /help - to get this message
Use        /info - to get information about the bot
       """
    )
