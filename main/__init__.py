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
SESSION="BQFmONcASNSlWTTCENlUwDdYnMbA4Vplog6_plkvjhA2v6I1oN_Z2rJcbPMQtSYMR90BlvynlSa3SSQz_sCxPYkm39ffXdO_k-TKpx-KlHMKN-qhL1wV1NgPJaephiAl4kBB1S9JRZP8fSiC5OUdhnpCMVqmY-ma5XBaSsXRLR41RMKlmp2VK4aJvg2fXCUJ4FHph6b96eqPdcLtjc0KqqU1altrPgfwwDh-_hPkx1rudtTle4BEJbJAtdXTsY7HMNqPQI7vxF88bejzYs9F0XdU_bjDIVhaghnw8g_J1TVUmvzMAjvjBmIuzsrXv_rNCMoTNLVb-P080qbI36LzHjy6DQ4I-gAAAAFQUsvEAA"
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
