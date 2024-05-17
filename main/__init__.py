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
BOT_TOKEN="6991118636:AAHfX1ErV-d4AXejHDQGB4mDQ0tBYZ6uGAE"

SESSION="BQGhN7YAxW8nU5629EFPT-6RrgRMybJxHTAZbWn-RVbTnYuBqRtK2EIVZkaUl30r5Tsju7vq8cCbv7q39V6b8k7wxMhxsi6qQYAi5x36VKdOcPUoCMt7XTShhSDhvYY2HIOifWr3Kwj0SQ0Ye0X2u4M2MTeIn9sOtNSXhdtYZ5OO7ox9AdeL53SsCPVLR_xtyAxzKwM8oYcqYHWrSOJP4VX91eSjuh4OOAiA0CsN2SmUiXIQP1EncilvdngUNlAhKIVDqyJKN7gNJJxylvNL5XE0DCshvsPV1J5TCjuoM2qLusN35q9t0GZ1ww9sYc-nsYEDB2rvx4-CEyl6HLYhdAk78wutWAAAAAF-8UZkAA"
#SESSION="AQDJqkIAJuQ4uL3pZvitdO9TzW4quNJ_ex_nEpnWR06gTsKW3CoFG-WvOYVZGjz7b84rx6dmXStPNOi-gYYyzIDmT1Q1xTWqNs4OMyPaggdkJPqWyKrVN3bHTxaleQ5B77axFsk7Q9T4teX1vzeJYmFG7WmvVNiG1cbvJEShhw6W69uYdGBnpTwmxSdyDsFkPaD8zPZvMz1ORvT3bWkb9LQSm8TUcRlJoY3ZPWVPlG0ChvvsPtf6VIyqszqtNjygrY1LpFbaOIuMX97gJ43yYBLyWW4My-bG2H3Oj69K6Ez_GRoRyWH2QQdyz3GGkRE3meBHblk4CctKp38Yeov9-oJaqUvN7QAAAAFSQG5zAA"


#SESSION="BQFmONcASNSlWTTCENlUwDdYnMbA4Vplog6_plkvjhA2v6I1oN_Z2rJcbPMQtSYMR90BlvynlSa3SSQz_sCxPYkm39ffXdO_k-TKpx-KlHMKN-qhL1wV1NgPJaephiAl4kBB1S9JRZP8fSiC5OUdhnpCMVqmY-ma5XBaSsXRLR41RMKlmp2VK4aJvg2fXCUJ4FHph6b96eqPdcLtjc0KqqU1altrPgfwwDh-_hPkx1rudtTle4BEJbJAtdXTsY7HMNqPQI7vxF88bejzYs9F0XdU_bjDIVhaghnw8g_J1TVUmvzMAjvjBmIuzsrXv_rNCMoTNLVb-P080qbI36LzHjy6DQ4I-gAAAAFQUsvEAA"
FORCESUB="MehulBots"
AUTH=5674921587
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
