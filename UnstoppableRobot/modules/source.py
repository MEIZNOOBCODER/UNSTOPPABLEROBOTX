from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from UnstoppableRobot import pbot as client


ANON = "https://telegra.ph/file/7bd111132fce009e4605e.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ᴜɴsᴛᴏᴩᴩᴀʙʟᴇ ʀᴏʙᴏᴛ](t.me/misslisa_robot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [•ᴜɴsᴛ🅞 ᴘᴘᴀʙʟᴇ•](tg://user?id=5369590180)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**•ᴜɴsᴛ🅞 ᴘᴘᴀʙʟᴇ•ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="tg://user?id=5369590180"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://github.com/S-UNSTOPPABLE/UNSTOPPABLE-ROBOT")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
