import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from UnstoppableRobot.events import register
from UnstoppableRobot import telethn as tbot


ALIVE_STUFF = [
    "https://telegra.ph/file/9c91d02c0b3ef63641963.mp4",
    "https://telegra.ph/file/a10878077476b20abdf23.mp4",
    "https://telegra.ph/file/d35409b383589b0199776.mp4",
    "https://telegra.ph/file/d1d8dbe8730178f258cf1.mp4",
    "https://telegra.ph/file/98e91150ca5942615f695.mp4",
    "https://telegra.ph/file/1e72c3b2532dad19332c3.mp4",
    "https://telegra.ph/file/415b0b67cf946ab5f3ec4.mp4",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\nɪ ᴀᴍ [•ᴜɴsᴛ🅞 ᴘᴘᴀʙʟᴇ•] ʟɪsᴀ​**\n\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [•ᴜɴsᴛ🅞 ᴘᴘᴀʙʟᴇ•](https://t.me/shaurya_here)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/misslisa_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/S_UNSTOPPABLE")]]
  anon_randi = random.choice(ALIVE_STUFF)
  await tbot.send_file(event.chat_id, anon_randi, caption=TEXT,  buttons=BUTTON)

## Alive mod
