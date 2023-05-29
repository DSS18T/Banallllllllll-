from RiZoeLX.functions import start_banall

from pyrogram import Client, filters

from pyrogram.types import Message

from dotenv import load_dotenv

import os

load_dotenv(".env")

api_id = int(os.getenv(" 6212330"))

api_hash = os.getenv("1dcf154704672a8c279126e1ecf229c3")

bot_token = os.getenv("6162480032:AAGQ_-EGxKGn4VWg-OvBdmJ_58wiyGfAzDI
")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.group & filters.command("banall"))

async def banall_members(client, message):

   await start_banall(client, message)

app.run()




















 


