# Credit © @AyiinXd
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# port by AyiinXd <https://t.me/AyiinXd>

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest


from AyiinXd import CMD_HELP
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd.utils import ayiin_cmd


@ayiin_cmd(pattern="telstring(?: |$)(.*)")
async def _(event):
    await event.edit("`Processing...`")
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        appid, apihash = event.pattern_match.group(1).split()

    else:
        await event.edit("**Yang Benerlah Kentod Biar Bisa Bikin Bot!!!**")
        return

    async with event.client.conversation("@AyiinStringRobot") as conv:
        try:
            await conv.send_message("/telethon")
            audio = await conv.get_response()
            await conv.send_message(appid)
            audio = await conv.get_response()
            await conv.send_message(apihash)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Mengirim Kode..")
            code = await event.get_reply_message()
            await conv.send_message(code)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("5065680852"))
            await conv.send_message("/telethon")
            audio = await conv.get_response()
            await conv.send_message(appid)
            audio = await conv.get_response()
            await conv.send_message(apihash)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Mengirim Kode..")
            code = await event.get_reply_message()
            await conv.send_message(code)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()


CMD_HELP.update(
    {
        "yinstring": f"**Plugin : **`yinstring`\
        \n\n  •  **Syntax :** `{cmd}telstring`\
        \n  •  **Function : **Untuk Membuat String Telethon.\
        \n\n**Untuk Membuat Bot Dari Bot Father, Ketik** `{cmd}buatbot < bot_name > < bot_username >`\
    "
    }
)
