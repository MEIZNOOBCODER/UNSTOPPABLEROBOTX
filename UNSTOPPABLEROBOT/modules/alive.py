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


PHOTO = [
    "https://te.legra.ph/file/a023c5a9071e18e406c3b.jpg",
    "https://telegra.ph/file/7bd111132fce009e4605e.jpg",
    "https://telegra.ph/file/804a5f9a3c32bac1ae15c.jpg",
    "https://telegra.ph/file/43edaa8914b7ce8998336.jpg",
    "https://telegra.ph/file/abed92d9b3ff409793324.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [•ᴜɴsᴛ🅞 ᴘᴘᴀʙʟᴇ•] ʟɪsᴀ​**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [•ᴜɴsᴛ🅞 ᴘᴘᴀʙʟᴇ•](https://t.me/shaurya_here)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/misslisa_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/S_UNSTOPPABLE")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
