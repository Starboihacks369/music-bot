from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Hero import db_mem


def url_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="â®",
                callback_data=f"slider B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ðµ",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ð¥",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="â¯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ð á´á´Êá´ Êá´sá´Êá´s",
                callback_data=f"Search {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ð¹ðððððððð¹", url=f"https://t.me/Best_friendsFor_Ever"
            ),
            InlineKeyboardButton(
                text="ð á´Êá´sá´ sá´á´Êá´Ê",
                callback_data=f"forceclose {query}|{user_id}",
            ),
        ],
    ]
    return buttons


def url_markup2(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="ðµ á´Êá´Ê á´á´sÉªá´",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ð¥ á´Êá´Ê á´ Éªá´á´á´",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ð á´Êá´sá´ sá´á´Êá´Ê",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="1ï¸â£", callback_data=f"Yukki {ID1}|{duration1}|{user_id}"
            ),
            InlineKeyboardButton(
                text="2ï¸â£", callback_data=f"Yukki {ID2}|{duration2}|{user_id}"
            ),
            InlineKeyboardButton(
                text="3ï¸â£", callback_data=f"Yukki {ID3}|{duration3}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="4ï¸â£", callback_data=f"Yukki {ID4}|{duration4}|{user_id}"
            ),
            InlineKeyboardButton(
                text="5ï¸â£", callback_data=f"Yukki {ID5}|{duration5}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="<", callback_data=f"popat 1|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="ð á´Êá´sá´", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text=">", callback_data=f"popat 1|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="6ï¸â£",
                callback_data=f"Yukki {ID6}|{duration6}|{user_id}",
            ),
            InlineKeyboardButton(
                text="7ï¸â£",
                callback_data=f"Yukki {ID7}|{duration7}|{user_id}",
            ),
            InlineKeyboardButton(
                text="8ï¸â£",
                callback_data=f"Yukki {ID8}|{duration8}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="9ï¸â£",
                callback_data=f"Yukki {ID9}|{duration9}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ð·ð¶ð",
                callback_data=f"Yukki {ID10}|{duration10}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="<", callback_data=f"popat 2|{query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="ð á´Êá´sá´", callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text=">", callback_data=f"popat 2|{query}|{user_id}"
            ),
        ],
    ]
    return buttons


def secondary_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="â¶ï¸", callback_data=f"resumecb"),
            InlineKeyboardButton(text="â¸ï¸", callback_data=f"pausecb"),
            InlineKeyboardButton(text="â­ï¸", callback_data=f"skipcb"),
            InlineKeyboardButton(text="â¹ï¸", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="ð á´á´Êá´ á´á´É´á´", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="ð á´Êá´sá´ á´á´É´á´", callback_data=f"close"),
        ],
    ]
    return buttons


def secondary_markup2(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="â¶ï¸", callback_data=f"resumecb"),
            InlineKeyboardButton(text="â¸ï¸", callback_data=f"pausecb"),
            InlineKeyboardButton(text="â­ï¸", callback_data=f"skipcb"),
            InlineKeyboardButton(text="â¹ï¸", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(text="ð á´Êá´sá´ á´á´É´á´", callback_data=f"close"),
        ],
    ]
    return buttons


def primary_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ------------------ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="â¶ï¸", callback_data=f"resumecb"),
            InlineKeyboardButton(text="â¸ï¸", callback_data=f"pausecb"),
            InlineKeyboardButton(text="â­ï¸", callback_data=f"skipcb"),
            InlineKeyboardButton(text="â¹ï¸", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="ð á´á´Êá´ á´á´É´á´", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="ð á´Êá´sá´ á´á´É´á´", callback_data=f"close"),
        ],
    ]
    return buttons


def timer_markup(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ------------------ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="â¶ï¸", callback_data=f"resumecb"),
            InlineKeyboardButton(text="â¸ï¸", callback_data=f"pausecb"),
            InlineKeyboardButton(text="â­ï¸", callback_data=f"skipcb"),
            InlineKeyboardButton(text="â¹ï¸", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="ð á´á´Êá´ á´á´É´á´", callback_data=f"other {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="ð á´Êá´sá´ á´á´É´á´", callback_data=f"close"),
        ],
    ]
    return buttons


def audio_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ------------------ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="â¶ï¸", callback_data=f"resumecb"),
            InlineKeyboardButton(text="â¸ï¸", callback_data=f"pausecb"),
            InlineKeyboardButton(text="â­ï¸", callback_data=f"skipcb"),
            InlineKeyboardButton(text="â¹ï¸", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="ð á´Êá´sá´ á´á´É´á´", callback_data=f"close")],
    ]
    return buttons


def audio_timer_markup_start(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{total_time} ------------------ {current_time}",
                callback_data=f"timer_checkup_markup {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(text="â¶ï¸", callback_data=f"resumecb"),
            InlineKeyboardButton(text="â¸ï¸", callback_data=f"pausecb"),
            InlineKeyboardButton(text="â­ï¸", callback_data=f"skipcb"),
            InlineKeyboardButton(text="â¹ï¸", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="ð á´Êá´sá´ á´á´É´á´", callback_data=f"close")],
    ]
    return buttons


audio_markup2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="â¶ï¸", callback_data=f"resumecb"),
            InlineKeyboardButton(text="â¸ï¸", callback_data=f"pausecb"),
            InlineKeyboardButton(text="â­ï¸", callback_data=f"skipcb"),
            InlineKeyboardButton(text="â¹ï¸", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton("ð á´Êá´sá´ á´á´É´á´", callback_data="close")],
    ]
)
