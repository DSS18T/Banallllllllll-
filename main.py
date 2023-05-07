from RiZoeLX.functions import start_banall

from pyrogram import Client, filters

from pyrogram.types import Message

@Client.on_message(filters.group & filters.command("banall"))

async def banall_members(Client, Message):

   await start_banall(Client, Message)























 


