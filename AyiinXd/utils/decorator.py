# Credits: @mrconfused
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import inspect
import re
from pathlib import Path

from telethon import events

from AyiinXd import (
    BL_CHAT,
    CMD_HANDLER,
    CMD_LIST,
    LOAD_PLUG,
    YINS2,
    YINS3,
    YINS4,
    YINS5,
    YINS6,
    YINS7,
    YINS8,
    YINS9,
    YINS10,
    SUDO_HANDLER,
    SUDO_USERS,
    bot,
    tgbot,
)


def ayiin_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global ayiin_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            ayiin_reg = sudo_reg = re.compile(pattern)
        else:
            ayiin_ = "\\" + CMD_HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            ayiin_reg = re.compile(ayiin_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = ayiin_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (ayiin_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        if bot:
            if not disable_edited:
                bot.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            bot.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if bot:
            if allow_sudo:
                if not disable_edited:
                    bot.add_event_handler(
                        func,
                        events.MessageEdited(
                            **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                        ),
                    )
                bot.add_event_handler(
                    func,
                    events.NewMessage(
                        **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                    ),
                )
        if YINS2:
            if not disable_edited:
                YINS2.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS2.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if YINS3:
            if not disable_edited:
                YINS3.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS3.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if YINS4:
            if not disable_edited:
                YINS4.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS4.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if YINS5:
            if not disable_edited:
                YINS5.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS5.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if YINS6:
            if not disable_edited:
                YINS6.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS6.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if YINS7:
            if not disable_edited:
                YINS7.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS7.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if YINS8:
            if not disable_edited:
                YINS8.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS8.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if YINS9:
            if not disable_edited:
                YINS9.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS9.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        if YINS10:
            if not disable_edited:
                YINS10.add_event_handler(
                    func, events.MessageEdited(**args, outgoing=True, pattern=ayiin_reg)
                )
            YINS10.add_event_handler(
                func, events.NewMessage(**args, outgoing=True, pattern=ayiin_reg)
            )
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def ayiin_handler(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args))
        if YINS2:
            YINS2.add_event_handler(func, events.NewMessage(**args))
        if YINS3:
            YINS3.add_event_handler(func, events.NewMessage(**args))
        if YINS4:
            YINS4.add_event_handler(func, events.NewMessage(**args))
        if YINS5:
            YINS5.add_event_handler(func, events.NewMessage(**args))
        if YINS6:
            YINS6.add_event_handler(func, events.NewMessage(**args))     
        if YINS7:
            YINS7.add_event_handler(func, events.NewMessage(**args))
        if YINS8:
            YINS8.add_event_handler(func, events.NewMessage(**args))
        if YINS9:
            YINS9.add_event_handler(func, events.NewMessage(**args))
        if YINS10:
            YINS10.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def asst_cmd(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/!]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def chataction(**args):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.ChatAction(**args))
        if YINS2:
            YINS2.add_event_handler(func, events.ChatAction(**args))
        if YINS3:
            YINS3.add_event_handler(func, events.ChatAction(**args))
        if YINS4:
            YINS4.add_event_handler(func, events.ChatAction(**args))
        if YINS5:
            YINS5.add_event_handler(func, events.ChatAction(**args))
        if YINS6:
            YINS6.add_event_handler(func, events.ChatAction(**args))
        if YINS7:
            YINS7.add_event_handler(func, events.ChatAction(**args))
        if YINS8:
            YINS8.add_event_handler(func, events.ChatAction(**args))
        if YINS9:
            YINS9.add_event_handler(func, events.ChatAction(**args))
        if YINS10:
            YINS10.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


def callback(**args):
    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator
