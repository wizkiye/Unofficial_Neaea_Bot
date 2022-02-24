from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from main import neaea
from neaea.neaea import RegistrationNumberNotFound


@Client.on_message(
    filters.regex(r"^\d{6}$")
)
async def reg_no(
        _: Client,
        message: Message
):
    reg_num = message.text
    try:
        result = await neaea.get_result(reg_no=reg_num)
    except RegistrationNumberNotFound:
        await message.reply_text("Registration Number NotFound")
        return
    sub_text = ""
    separator = "﹍" * 15 + "\n"
    subjects = result.get_subjects()
    for subject in subjects:
        sub_text += f"**{subject.subject_name} ({subject.subject_abbr}) **: `{subject.mark}`\n"
        sub_text += separator
    text = f"""
**Reg No**:  `{result.registration_number}`
**Name**:    `{result.name}`
**ID**:            `{result.id}`
**Gender**:  `{result.gender}`
**Stream**:  `{result.stream}`
**School**:   `{result.school}`
{separator}
                 **Exam Results**
{separator}
{sub_text}

                  **Total**: **{result.total}**
    """
    await message.reply_text(
        text,
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"{emoji.LINK} Share!",
                        switch_inline_query=str(result.registration_number)
                    )
                ]
            ]
        )
    )
