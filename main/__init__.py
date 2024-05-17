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

SESSION="BQGhN7YAPKfnpIYuPN7cmeHsOHmGwOT1CAWmBwjP-tb2sqqp3S1UBsdCDzpcgGMbgh2yAVMxXL0tdz2gKctGnzEsnrAmgdOuMLitzOCqkkgKvWviYC1LQyn69K4l90ZsplMHmThMc_oJf32z8FJIAjmE3M7S98AOctL1yIXzRkrnvKnMgOmFxBDiLDhOYLAVQrSNrA-mqWj9dQIx8SomPBiOw2a3U-NE_CbiA3KeZDAtU3u_o2hiF3LtofiRWGMlmjpI5g-gLj4puwqRZ7hv0FYk4FMDLgR79Uwq0d-UlMGqxaD9mmlk-wS5v3VUwbb3pK2zr2eyeUIhzBg0t5uyBYZN22oB9gAAAAF-8UZkAA"
#SESSION="AQDJqkIAeRm_Rtdur4xDwf88Uroyo-SEr3xuRCd5PiOn71-p4kmVPPM4g9R1ck3U0Lfv6PzY0TQZQUWx1jh83dtI7aTe5aYRleqYmTIL4zcUbRHWF7VxpBfXC8qxVasScayBkc17311ODCJh6dNbqtvytK5zA3ypnWvuo5bLz-UOAIERm2HP2rjknu3k6-xzFAE3U4NvllO5Ke23C_MtgfXnohILOuwgMyq78jgaNMCvFeWyHEkNIYZ_I61zq9h5VioByuMa7_W4Jng20rqsoCD-fkgi5CngWOJmyodU3LB8srG7opdjqAljUA-khAA9rqgfeiex3HBH8L70qH0JonEpEgvm7QAAAAFSQG5zAA"


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
