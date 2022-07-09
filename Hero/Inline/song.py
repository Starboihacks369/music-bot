from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def song_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"song_right B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⬇️ ᴅᴏᴡɴʟᴏᴀᴅ",
                callback_data=f"qwertyuiopasdfghjkl {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"song_right F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌹𝐒𝐔𝐏𝐏𝐎𝐑𝐓🌹", url=f"https://t.me/Best_friendsFor_Ever"
            ),
            InlineKeyboardButton(
                text="🗑 ᴄʟᴏsᴇ sᴇᴀʀᴄʜ",
                callback_data=f"forceclose {query}|{user_id}",
            )
        ],
    ]
    return buttons


def song_download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⬇️ ɢᴇᴛ ᴀᴜᴅɪᴏ",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⬇️ ɢᴇᴛ ᴠɪᴅᴇᴏ",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑 ᴄʟᴏsᴇ ᴍᴇɴᴜ",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
