from pyrogram import Client, filters
from pyrogram.types import Message

import config
from main import mongo


@Client.on_message(
    filters.user(config.ADMIN) & filters.command(["send_msg"])
)
async def send_msg_to_all(
        client: Client,
        message: Message
):
    msg = message.text.replace("/send_msg", "")
    users = await mongo.find_all(
        collection='USERS',
        post={
            'chat_id': 1,
            'username': 1,
        }
    )
    if msg:
        for user in users:
            await client.send_message(
                chat_id=user['chat_id'],
                text=msg
            )
    else:
        await message.reply_text(
            text="Message is empty"
        )
