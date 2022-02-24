from pyrogram import Client, filters

from main import mongo


@Client.on_message(
    filters.command(['start'])
)
async def start(_, message):
    if not await mongo.find_one("USERS", {'chat_id': message.chat.id}):
        await mongo.insert(
            "USERS", {
                'chat_id': message.chat.id,
                'username': message.chat.username,
                'first_name': message.chat.first_name,
                'last_name': message.chat.last_name,
                'is_verified': message.chat.is_verified,
                'is_restricted': message.chat.is_restricted,
                'is_scam': message.chat.is_scam,
                'is_support': message.chat.is_support,
                "date": message.date
            }
        )
    await message.reply_text(
        text="""
        Hi, I'm a bot that can help you to see your Neaea Exam result.\n
You can use /help to see the list of commands.
or You can send your registration number to see your result.
        """
    )
