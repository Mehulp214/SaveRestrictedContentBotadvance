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
BOT_TOKEN="7189262900:AAGn9K0Yh4N3LQd4QQm8M84tcIrafK130uE"

SESSION = "BQDJqkIArL1laKfzxNPmALXY3N1adSUBN90y2pIzYm0ExGag-gIrU3zc8bJ8GYxE7hV_9IkFAqSqeec0xGyfQVdpplyM_kWXkMyYFaYJOpX81tYTu5N2e6B8y71c16_E8u5Ztl-2pcESei-RPQLxaHrVL2WoBGqjRn9-ILPWDx-3QQIPqCKOJ6n0RMczacx7DIphWWoHWTgl_JDWj0GqDN59DMB5BGpSr5_3ypmqeMhyh9wZGI5M2tDZJ6K6VKgmJYBbLaaNYg3fVeuRance8m1O4JaQPdUprzc4xgqdROJDFJnmzudF98hpqT8Iqux9Gri8Zjcu84jGaAXbS0JM6fbB66BKvgAAAAGdfGRoAA"
#SESSION="AQDJqkIAJuQ4uL3pZvitdO9TzW4quNJ_ex_nEpnWR06gTsKW3CoFG-WvOYVZGjz7b84rx6dmXStPNOi-gYYyzIDmT1Q1xTWqNs4OMyPaggdkJPqWyKrVN3bHTxaleQ5B77axFsk7Q9T4teX1vzeJYmFG7WmvVNiG1cbvJEShhw6W69uYdGBnpTwmxSdyDsFkPaD8zPZvMz1ORvT3bWkb9LQSm8TUcRlJoY3ZPWVPlG0ChvvsPtf6VIyqszqtNjygrY1LpFbaOIuMX97gJ43yYBLyWW4My-bG2H3Oj69K6Ez_GRoRyWH2QQdyz3GGkRE3meBHblk4CctKp38Yeov9-oJaqUvN7QAAAAFSQG5zAA"


#SESSION="BQFmONcASNSlWTTCENlUwDdYnMbA4Vplog6_plkvjhA2v6I1oN_Z2rJcbPMQtSYMR90BlvynlSa3SSQz_sCxPYkm39ffXdO_k-TKpx-KlHMKN-qhL1wV1NgPJaephiAl4kBB1S9JRZP8fSiC5OUdhnpCMVqmY-ma5XBaSsXRLR41RMKlmp2VK4aJvg2fXCUJ4FHph6b96eqPdcLtjc0KqqU1altrPgfwwDh-_hPkx1rudtTle4BEJbJAtdXTsY7HMNqPQI7vxF88bejzYs9F0XdU_bjDIVhaghnw8g_J1TVUmvzMAjvjBmIuzsrXv_rNCMoTNLVb-P080qbI36LzHjy6DQ4I-gAAAAFQUsvEAA"
FORCESUB="jingalalahuhu1"
AUTH=6937142376
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
