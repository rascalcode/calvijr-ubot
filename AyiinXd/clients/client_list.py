# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, YINS2, YINS3, YINS4, YINS5, YINS6, YINS7, YINS8, YINS9, YINS10):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if YINS2 is not None:
            id2 = await YINS2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if YINS3 is not None:
            id3 = await YINS3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if YINS4 is not None:
            id4 = await YINS4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if YINS5 is not None:
            id5 = await YINS5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    try:
        if YINS6 is not None:
            id6 = await YINS6.get_me()
            user_ids.append(id6.id)
    except BaseException:
        pass

    try:
        if YINS7 is not None:
            id7 = await YINS7.get_me()
            user_ids.append(id7.id)
    except BaseException:
        pass

    try:
        if YINS8 is not None:
            id8 = await YINS8.get_me()
            user_ids.append(id8.id)
    except BaseException:
        pass

    try:
        if YINS9 is not None:
            id9 = await YINS9.get_me()
            user_ids.append(id9.id)
    except BaseException:
        pass

    try:
        if YINS10 is not None:
            id10 = await YINS10.get_me()
            user_ids.append(id10.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTcwMDQwNTczMg==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        YINS_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        YINS_USER = client.first_name
    yins_mention = f"[{YINS_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, YINS_USER, yins_mention
