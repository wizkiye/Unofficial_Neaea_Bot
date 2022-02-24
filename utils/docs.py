from pyrogram import emoji
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

import neaea
from config import BOT_USERNAME

FIRE_THUMB = "https://i.imgur.com/qhYYqZa.png"
ROCKET_THUMB = "https://i.imgur.com/PDaYHd8.png"
ABOUT_BOT_THUMB = "https://i.imgur.com/zRglRz3.png"
OPEN_BOOK_THUMB = "https://i.imgur.com/v1XSJ1D.png"
RED_HEART_THUMB = "https://i.imgur.com/66FVFXz.png"
SCROLL_THUMB = "https://i.imgur.com/L1u0VlX.png"
USER_THUMB = "https://i.imgur.com/3r8jnp5.png"

ABOUT = (
    "**Unofficial Neaea Telegram Bot**\n"
    "**Created by**: [By this dude](https://github.com/wizkiye)\n"
    "**Source code**: [here](https://github.com/wizkiye/Unofficial_Neaea_Bot)\n"
    "`Don't forget to star the repo if you like it!`\n"
    "**Bot version**: __1.0.0__\n"
    "**Secret link**: [https://neaeahacked.com](https://m.youtube.com/watch?v=dQw4w9WgXcQ)\n"
)
DEFAULT_RESULTS = [
    InlineQueryResultArticle(
        title="About this Bot",
        input_message_content=InputTextMessageContent(
            ABOUT,
            disable_web_page_preview=True,
            parse_mode="markdown"
        ),
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                f"{emoji.CARD_INDEX_DIVIDERS} Source Code",
                url="https://github.com/wizkiye/Unofficial_Neaea_Bot"
            ),
            InlineKeyboardButton(
                f"{emoji.FIRE} Search!",
                switch_inline_query=""
            )
        ]]),
        description="About Unofficial Neaea Bot ",
        thumb_url=ABOUT_BOT_THUMB,
    ),
    InlineQueryResultArticle(
        title="Quick Start",
        input_message_content=InputTextMessageContent(
            f"{emoji.ROCKET} **Quick Search**\n\n"
            f"Send your registration number to get the result.\n\teg:\n"
            f"\t\t\t`123456`\n"
            f"\t\t\tor {BOT_USERNAME} 123456\n\n"
            f"**Note**: Registration number must be 6 digits long.\n\n",
            disable_web_page_preview=True,
        ),
        description="Quick overview to get you started as fast as possible.",
        thumb_url=ROCKET_THUMB,
    ),
    InlineQueryResultArticle(
        title="Support",
        input_message_content=InputTextMessageContent(
            f"{emoji.RED_HEART} **Support Us**\n\n"
            f"[Support](https://github.com/wizkiye/Unofficial_Neaea_Bot) - By 🌟 staring the repo in github [here]("
            f"https://github.com/wizkiye/Unofficial_Neaea_Bot)\n\n "
            f"`Ways to show your appreciation.`",
            disable_web_page_preview=True,
        ),
        description="Ways to show your appreciation.",
        thumb_url=RED_HEART_THUMB,
    ),
]


def get_result_text(result: neaea.Result):
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
    return [
        InlineQueryResultArticle(
            title=result.name,
            input_message_content=InputTextMessageContent(
                text,
                disable_web_page_preview=True,
                parse_mode="markdown",

            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            f"{emoji.LINK} Share!",
                            switch_inline_query=str(result.registration_number)
                        )
                    ]
                ]
            ),
            description="Result for {}".format(result.name),
            thumb_url=USER_THUMB,
        ),

    ]
