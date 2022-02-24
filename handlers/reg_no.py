from neaea.neaea import RegistrationNumberNotFound
from pyrogram import Client, filters
from pyrogram.types import Message

from main import neaea


@Client.on_message(
    filters.regex(r"\d{6}")
)
async def reg_no(
        _: Client,
        message: Message
):
    reg_num = message.text
    try:
        result = await neaea.get_result(reg_no=reg_num)
    except RegistrationNumberNotFound:
        await message.reply_text("RegistrationNumberNotFound")
        return
    sub_text = ""
    separetor = "﹍" * 15 + "\n"
    subjects = result.get_subjects()
    for subject in subjects:
        sub_text += f"**{subject.subject_name} ({subject.subject_abbr}) **: `{subject.mark}`\n"
        sub_text += separetor
    text = f"""
**Reg No**:  `{result.registration_number}`
**Name**:    `{result.name}`
**ID**:            `{result.id}`
**Gender**:  `{result.gender}`
**Stream**:  `{result.stream}`
**School**:   `{result.school}`
{separetor}
                 **Exam Results**
{separetor}
{sub_text}

                  **Total**: **{result.total}**
    """
    await message.reply_text(
        text,
        parse_mode="markdown"
    )
