# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

from telethon.utils import get_peer_id

from AyiinXd import BOT_TOKEN
from AyiinXd import BOT_VER as version
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    YINS2,
    YINS3,
    YINS4,
    YINS5,
    YINS6,
    YINS7,
    YINS8,
    YINS9,
    YINS10,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_6,
    STRING_7,
    STRING_8,
    STRING_9,
    STRING_10,
    STRING_SESSION,
    blacklistayiin,
    bot,
    call_py,
    tgbot,
)
from AyiinXd.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nMan-UserBot v{}, Copyright © 2021-2022 ʀɪsᴍᴀɴ• <https://github.com/mrismanaziz>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nMan-UserBot v{}, Copyright © 2021-2022 ʀɪsᴍᴀɴ• <https://github.com/mrismanaziz>"


async def yins_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multiyins():
    if 1700405732 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001675396283 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1700405732 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(yins_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_2:
        try:
            YINS2.start()
            LOOP.run_until_complete(yins_client(YINS2))
            user = YINS2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            YINS3.start()
            LOOP.run_until_complete(yins_client(YINS3))
            user = YINS3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            YINS4.start()
            LOOP.run_until_complete(yins_client(YINS4))
            user = YINS4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            YINS5.start()
            LOOP.run_until_complete(yins_client(YINS5))
            user = YINS5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_6:
        try:
            YINS6.start()
            LOOP.run_until_complete(yins_client(YINS6))
            user = YINS6.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_6 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_7:
        try:
            YINS7.start()
            LOOP.run_until_complete(yins_client(YINS7))
            user = YINS7.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_7 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_8:
        try:
            YINS8.start()
            LOOP.run_until_complete(yins_client(YINS8))
            user = YINS8.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_8 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_9:
        try:
            YINS9.start()
            LOOP.run_until_complete(yins_client(YINS9))
            user = YINS9.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_9 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_10:
        try:
            YINS10.start()
            LOOP.run_until_complete(yins_client(YINS10))
            user = YINS10.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_10 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistayiin:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    if not STRING_6:
        failed += 1
    if not STRING_7:
        failed += 1
    if not STRING_8:
        failed += 1
    if not STRING_9:
        failed += 1
    if not STRING_10:
        failed += 1
    return failed
