# Credit © @AyiinXd
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# port by AyiinXd <https://t.me/AyiinXd>

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest


from AyiinXd import CMD_HELP
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd.utils import ayiin_cmd


@ayiin_cmd(pattern="tel( no| code| verif|$)(.*)")
async def _(event):
    await event.edit("`Processing...`")
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        appid, apihash = event.pattern_match.group(1).split()

    else:
        await event.edit("**Yang Benerlah Kentod Biar Bisa Bikin Bot!!!**")
        return

    async with event.client.conversation("@YinsRobot") as conv:
        try:
            await conv.send_message("/start")
            audio = await conv.get_response()
            await conv.send_message("/telethon")
            audio = await conv.get_response()
            audio = await conv.get_response()
            await conv.send_message(appid)
            audio = await conv.get_response()
            await conv.send_message(apihash)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan No Hp...")
        except YouBlockedUserError:
            await event.client(UnblockRequest("5260657154"))
            await conv.send_message("/start")
            audio = await conv.get_response()
            await conv.send_message("/telethon")
            audio = await conv.get_response()
            audio = await conv.get_response()
            await conv.send_message(appid)
            audio = await conv.get_response()
            await conv.send_message(apihash)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan No Hp...")

    if appid == "no"
            await event.edit("`Processing...`")
            async with event.client.conversation("@YinsRobot") as conv:
            code = await event.get_reply_message()
            await client.send_message("@YinsRobot", f"{code}")
            audio = await conv.get_response()
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan Kode...")
            code = await event.get_reply_message()
            await client.send_message("@YinsRobot", f"{code}")
            audio = await conv.get_response()
            two_verif = await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan Kode...")
            code = await event.get_reply_message()
            await client.send_message("@YinsRobot", f"{code}")
            audio = await conv.get_response()
            two_verif = await event.client.forward_messages(event.chat_id, audio)
            await event.delete()


@ayiin_cmd(pattern="pyrostring(?: |$)(.*)")
async def _(event):
    await event.edit("`Processing...`")
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        appid, apihash = event.pattern_match.group(1).split()

    else:
        await event.edit("**Yang Benerlah Kentod Biar Bisa Bikin Bot!!!**")
        return

    async with event.client.conversation("@YinsRobot") as conv:
        try:
            await conv.send_message("/start")
            audio = await conv.get_response()
            await conv.send_message("/pyrogram")
            audio = await conv.get_response()
            audio = await conv.get_response()
            await conv.send_message(appid)
            audio = await conv.get_response()
            await conv.send_message(apihash)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan No Hp...")
            code = await event.get_reply_message()
            await conv.send_message(code)
            audio = await conv.get_response()
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan Kode...")
            code = await event.get_reply_message()
            await conv.send_message(code)
            audio = await conv.get_response()
            two_verif = await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan Kode...")
            code = await event.get_reply_message()
            await conv.send_message(code)
            audio = await conv.get_response()
            two_verif = await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("5260657154"))
            await conv.send_message("/start")
            audio = await conv.get_response()
            await conv.send_message("/pyrogram")
            audio = await conv.get_response()
            audio = await conv.get_response()
            await conv.send_message(appid)
            audio = await conv.get_response()
            await conv.send_message(apihash)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan No Hp...")
            code = await event.get_reply_message()
            await conv.send_message(code)
            audio = await conv.get_response()
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan Kode...")
            code = await event.get_reply_message()
            await conv.send_message(code)
            audio = await conv.get_response()
            two_verif = await event.client.forward_messages(event.chat_id, audio)
            await event.reply("Silahkan Reply Pesan Untuk Memasukkan Kode...")
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
