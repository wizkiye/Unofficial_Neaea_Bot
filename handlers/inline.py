import re

from pyrogram import Client
from pyrogram import emoji
from pyrogram.types import InlineQuery

import neaea as Neaea
from main import neaea
from utils import docs

CACHE_TIME = 5


@Client.on_inline_query()
async def inline_handler(_, query: InlineQuery):
    string = query.query.lower()

    if string == "":
        await query.answer(
            results=docs.DEFAULT_RESULTS,
            cache_time=CACHE_TIME,
            switch_pm_text=f"{emoji.MAGNIFYING_GLASS_TILTED_RIGHT} Type to search Students",
            switch_pm_parameter="start",
        )

        return
    if re.match(r"^ *\d{1,5}$", string):
        await query.answer(
            results=[],
            cache_time=CACHE_TIME,
            switch_pm_text=f'{emoji.CROSS_MARK} Reg Number Must Be 6 Digits... "{string}"',
            switch_pm_parameter="okay",
        )
    if re.match(r"^ *\d{6}$", string):
        try:
            results = await neaea.get_result(string)
            await query.answer(
                results=docs.get_result_text(results),
                cache_time=CACHE_TIME,
                switch_pm_text=f"{emoji.CHECK_MARK} Results for {string}",
                switch_pm_parameter="start",
            )
        except Neaea.RegistrationNumberNotFound:
            await query.answer(
                results=[],
                cache_time=CACHE_TIME,
                switch_pm_text=f'{emoji.CROSS_MARK} Registration Number NotFound "{string}"',
                switch_pm_parameter="okay",
            )
