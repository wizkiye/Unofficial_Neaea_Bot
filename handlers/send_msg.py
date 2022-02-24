from pyrogram import Client, filters
from pyrogram.types import Message

import config
from main import mongo


@Client.on_message(
    filters.user(config.ADMIN) & filters.command(["send_msg"])
)
async def send_msg_to_one(
        client: Client,
        message: Message
):
    user_msg = message.text.replace("/send_msg ", "").split(" ")
    chat_id, msg = user_msg[0], " ".join(user_msg[1:])
    if not chat_id:
        await message.reply_text(
            "Chat id Not Specified"
        )
        return

    if not msg:
        await message.reply_text(
            "Message Not Specified"
        )
        return

    if user := await mongo.find_one(
            collection='USERS',
            post={
                'chat_id': int(chat_id),
            }
    ):
        await client.send_message(
            chat_id=user['chat_id'],
            text=msg
        )
    else:
        await message.reply_text(
            "User Not Found"
        )


@Client.on_message(
    filters.user(config.ADMIN) & filters.command(["send_msg_to_all"])
)
async def send_msg_to_all(
        client: Client,
        message: Message
):
    msg = message.text.replace("/send_msg", "")
    if not msg:
        await message.reply_text(
            "Message Not Specified"
        )
        return

    users = await mongo.find_all(
        collection='USERS',
        post={
            'chat_id': 1,
            'username': 1,
        }
    )
    users_count = users.__len__()
    text = (
        f"Sending Message To {users_count} Users"
    )
    await message.reply_text(
        text
    )
    _msg = await message.reply_text(
        f"Sent To 0/{users_count} Users"
    )
    for i, user in enumerate(users):
        await client.send_message(
            chat_id=user['chat_id'],
            text=msg
        )
        await _msg.edit_text(
            text=f"Sent To {i}/{users_count} Users"
        )
