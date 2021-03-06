# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================Γ========================
#            Jangan Hapus Credit Ngentod
# ========================Γ========================

import io
from datetime import datetime as dt

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import BOTLOG_CHATID, CMD_HELP
from AyiinXd.events import register
from AyiinXd.utils import ayiin_cmd, edit_delete, edit_or_reply, reply_id


@ayiin_cmd(pattern="btpm(?: |$)(.*)")
async def listbtpm(list):
    ayiin = await edit_or_reply(list, "`Processing...`")
    input = list.pattern_match.group(1)
    if not input:
        return await edit_delete(list, "**[error] - Isi Username Ch Kentod...**")
    p = await list.client.get_entity(input)
    d_form = "%d - %B - %Y"
    user = await list.client.get_me()
    await ayiin.edit(f"**π±ππΏπΌ π²π·:** {p.title}\n"
                     f"**ππ°π½πΆπΆπ°π» : {dt.now().strftime(d_form)}**\n\n"
                     f"**π°π³πΌπΈπ½ : @{user.username}**\n"
                     f"**π²π·: {p.username}**\n"
                     f"**----------------------------------**\n"
                     f"**β’ πΆπΆ.πΆπΆ - πΆπΈ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ πΆπΈ.πΆπΆ - πΆπΊ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ πΆπΊ.πΆπΆ - πΆπΌ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ πΆπΌ.πΆπΆ - πΆπΎ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ πΆπΎ.πΆπΆ - π·πΆ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ π·πΆ.πΆπΆ - π·πΈ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**----------------------------------------------**\n"
                     f"**β’ π·πΈ.πΆπΆ - π·πΊ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ π·πΊ.πΆπΆ - π·πΌ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ π·πΌ.πΆπΆ - π·πΎ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ π·πΎ.πΆπΆ - πΈπΆ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ πΈπΆ.πΆπΆ - πΈπΈ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**β’ πΈπΈ.πΆπΆ - πΆπΆ.πΆπΆ : **\n"
                     f"**-π°π³πΌπΈπ½ : **\n"
                     f"**-----------------------------------------------**\n"
                     f"**βπΌππ πΈ πππ πππππ ππππ ππππππππ ππππ**\n"
                     f"**βπΊπππππ ππππ π· π πΈπΊ πππ**\n"
                     f"**βοΈπ½πΎ ππ·πΎπππ»πΈπ½πΊ**")


@register(outgoing=True,
          pattern=r"\$\w*",
          ignore_unsafe=True,
          disable_errors=True)
async def on_btpm(event):
    """ Fbtpm logic. """
    try:
        from AyiinXd.ayiinxd.btpm_ayiin import get_btpm
    except AttributeError:
        return
    name = event.text[1:]
    btpm = get_btpm(name)
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    if btpm and btpm.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(btpm.f_mesg_id))
        await event.client.send_message(event.chat_id,
                                        msg_o.message,
                                        reply_to=message_id_to_reply,
                                        file=msg_o.media)
        await event.delete()
    elif btpm and btpm.reply:
        await event.client.send_message(event.chat_id,
                                        btpm.reply,
                                        reply_to=message_id_to_reply)
        await event.delete()


@ayiin_cmd(pattern=r"savebt (\w*)")
async def on_btpm_save(event):
    """ For .savebt command, saves btpm for future use. """
    try:
        from AyiinXd.ayiinxd.btpm_ayiin import add_btpm
    except AtrributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    keyword = event.pattern_match.group(1)
    string = event.text.partition(keyword)[2]
    msg = await event.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#BTPM\
            \nKEYWORD: {keyword}\
            \n\n**Pesan berikut disimpan sebagai data untuk btpm, JANGAN dihapus!!!**"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                "**Menyimpan list btpm dengan media memerlukan BOTLOG_CHATID untuk disetel.**"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "**Daftar Btpm {} Disimpan. Gunakan** `${}` **di mana saja untuk menggunakannya**"
    if add_btpm(keyword, string, msg_id) is False:
        await event.edit(success.format("Diperbarui", keyword))
    else:
        await event.edit(success.format("Berhasil", keyword))


@ayiin_cmd(pattern="listbt$")
async def on_btpm_list(event):
    """ For .listbt command, list btpm saved by you. """
    try:
        from AyiinXd.ayiinxd.btpm_ayiin import get_fbtpm
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return

    message = "Daftar Btpm yang tersedia :\n\n"
    all_fbtpm = get_fbtpm()
    for lbtpm in all_fbtpm:
        if message == "**Tidak ada daftar btpm yang tersedia saat ini.**":
            message = "Daftar Btpm yang tersedia :\n\n"
            message += f"`${lbtpm.btpm}`\n"
        else:
            message += f"`${lbtpm.btpm}`\n"

    await event.edit(message)


@ayiin_cmd(pattern=r"delbt (\w*)")
async def on_btpm_delete(event):
    """ For .delbt command, deletes a list btpm. """
    try:
        from AyiinXd.ayiinxd.btpm_ayiin import remove_btpm
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    name = event.pattern_match.group(1)
    if remove_btpm(name) is True:
        await event.edit(f"**Berhasil menghapus daftar btpm:** `{name}`")
    else:
        await event.edit(f"**Tidak dapat menemukan daftar btpm:** `{name}`")



# ========================Γ========================
#            Jangan Hapus Credit Ngentod
# ========================Γ========================


CMD_HELP.update(
    {
        "btpmayiin": f"**Plugin:** `btpmayiin`\
        \n\n  β’ **Perintah :** `{cmd}btpm` <nama_ch (TanpaSpasi)> <username ch>\
        \n  β’  **Kegunaan :** __Untuk Mendapatkan List Btpm Kosong.__\
        \n\n  β’ **Perintah :** `{cmd}savebt` <nama_list>\
        \n  β’  **Kegunaan :** __Untuk Menyimpan List Btpm.__\
        \n\n  β’ **Perintah :** `{cmd}$`<nama_list>\
        \n  β’  **Kegunaan :** __Untuk Mendapatkan List Btpm Yang Tersimpan.__\
        \n\n  β’ **Perintah :** `{cmd}delbt` <nama_list>\
        \n  β’  **Kegunaan :** __Menghapus List Btpm Yang Tersimpan.__\
        \n\n  β’ **Perintah :** `{cmd}listbt` <nama_list>\
        \n  β’  **Kegunaan :** __Untuk Menlihat Semua List Btpm Yang Tersimpan.__\
    "
    }
)
