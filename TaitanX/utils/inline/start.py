from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from TaitanX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ⁣𝔸DD 𝕄E 𝕋O 𝕐OUƦ 𝔾ƦOUק ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=" ℂᴏᴍᴍᴀɴᴅʟᴇℝ ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text=" 𝕊ᴇᴛᴛɪɴɢꜱ ", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text=" 𝔾ʀᴏᴜ𝕡 ", url=f"https://t.me/timepassgroup01"),
            InlineKeyboardButton(
                text=" 𝕊ᴜᴘᴘᴏʀ𝕋 ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" 𓆩𝔸DD 𝕄E 𝕋O 𝕐OUƦ 𝔾ƦOUק𓆪 ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=" ℂᴏᴍᴍᴀɴᴅʟᴇℝ ", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text=" 𝔾ʀᴏᴜ𝕡 ", url=f"https://t.me/timepassgroup01"),
            InlineKeyboardButton(
                text=" 𝕊ᴜᴘᴘᴏʀ𝕋 ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="𓊈𒆜𝓞𝔀𝓷𝓮𝓻𒆜𓊉", url=f"https://t.me/TaitanGamer"
                 )
        ],
     ]
    return buttons
