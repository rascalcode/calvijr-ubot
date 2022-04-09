# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from AyiinXd import BOT_VER as version
from AyiinXd import BOTLOG_CHATID
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import YINS2, YINS3, YINS4, YINS5, YINS6, YINS7, YINS8, YINS9, YINS10, bot, branch, tgbot
from AyiinXd.utils import checking

MSG_ON = """
✨ **Ayiin-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** {}
➠ @{}
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def ayiin_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            YinsUBOT = await tgbot.get_me()
            BOT_USERNAME = YinsUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            YinsUBOT = await tgbot.get_me()
            BOT_USERNAME = YinsUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "Assɪsᴛᴀɴᴛ Aʏɪɪɴ"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS2:
            await checking(YINS2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS3:
            await checking(YINS3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS4:
            await checking(YINS4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS5:
            await checking(YINS5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS6:
            await checking(YINS6)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS6.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS7:
            await checking(YINS7)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS7.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS8:
            await checking(YINS8)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS8.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS9:
            await checking(YINS9)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS9.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if YINS10:
            await checking(YINS10)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await YINS10.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
