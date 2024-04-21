#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#API_ID = config("API_ID", default=None, cast=int)
#API_HASH = config("API_HASH", default=None)
#BOT_TOKEN = config("BOT_TOKEN", default=None)
#SESSION = config("SESSION", default=None)
#FORCESUB = config("FORCESUB", default=None)
#AUTH = config("AUTH", default=None, cast=int)

API_ID=23476439
API_HASH="1626e884119a29dbccbb78e39b48128f"
BOT_TOKEN="7079929259:AAEC6jQzSzAPolYhL4nwExldNlIKf4sRcjU"
SESSION="1BVtsOKYBu62W0wsH5hJUF3JsSktmNpVHhCUAVc48fVVDs0nFEd0h9u_ih-2iEVwoWAP_XD0_Sg8ELZ8iV0BxkAHHyfOTBcojOHGF3wTg61VcU5TrVHxnJ8NrQs-dYVNJ0nS2sjnZFKBEb5pn33lrYe-aQfG0o06k1pe8eOa37P9nRw0GPQpjws1-3CqpAkXHZDfimknwEbU-My6j-0UJz2tKCJyD2rI7XVM0gBTKjsQ-oaMTYLJNkYn3Jthr3S-PAuDIb7ohLlpq_k96CPM5GSfhiJGGux0QSrtHVfdqn8SLack9eQ6ZymMwKbdzFiKwRtooTWHi3MEvMe_UBXoqt8Gm0SKEGSA="
FORCESUB="MehulBots"
AUTH=5434500969
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
