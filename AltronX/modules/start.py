from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("𝐂ᴏᴍᴍᴀɴᴅs", data="help_back")
        ],
        [
        Button.url("𝐂ʜᴀɴɴᴇʟ", "https://t.me/honey_networks"),
        Button.url("𝐌ᴜsɪᴄ", "https://t.me/Akame_musicbot")
        ],
        [
        Button.url("𝐎ᴡɴᴇʀ", "https://t.me/OgHoneyy")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝗛𝗘𝗬 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ  [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ ᴅᴇᴠᴇʟᴏᴘᴇʀ :~ [𝐇𝐎𝐍𝐄𝐘](https://t.me/OgHoneyy)**\n\n"
        TEXT += f"» **ʜᴏɴᴇʏ sᴘᴀᴍ ᴠᴇʀsɪᴏɴ :** `3.2`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/fc1e5be675ae50ef962c1.jpg",
                caption=TEXT, 
                buttons=PythonButton)
