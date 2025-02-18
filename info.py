import re, os
from os import environ, getenv
from Script import script
import asyncio
from logging import WARNING, getLogger
from pyrogram import Client
from time import time
import logging 

LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)
getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '21872096'))
API_HASH = environ.get('API_HASH', 'cf080f74cbc7f619e5e6e5cea9b2a532')
OWNER_ID = environ.get('OWNER_ID', '5829414900')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/5e1f8888547a1a896a902.jpg https://graph.org/file/9649c1dcbae09f2e7700e.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/8f68ce426acfb8b60b229-7e69cb6037affc581b.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/8f68ce426acfb8b60b229-7e69cb6037affc581b.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/8f68ce426acfb8b60b229-7e69cb6037affc581b.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/43f25856bde8cdfe2264c-808110c884c898f41d.jpg'))
CODE = (environ.get('CODE', 'https://graph.org/file/0aeb02b9f3b0d4f332454-ff66af6532d612599a.jpg'))


# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
PREFIX = environ.get("PREFIX", "/")

# for eval function, work only in a specific group
EVAL_ID = environ.get("EVAL_ID", "-1002309567480")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5829414900').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002168629899').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '7383009157').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1002213129805') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002169094300') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002286029827') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True)) # True if you want no results messages in Log Channel

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://G:G@cluster0.sdtu7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#chatgptAI
AI = is_enabled((environ.get("AI","True")), True)
OPENAI_API = environ.get("OPENAI_API", "5d117836e00643c696176a9548b2f134")
GOOGLE_API_KEY = environ.get("GOOGLE_API_KEY", "AIzaSyD214hhYJ-xf8rfaWX044_g1VEBQ0ua55Q") #DON'T REMOVE ANYTHING!! @CREDIT @SD_BOTS
AI_LOGS = int(environ.get("AI_LOGS", "-1002451523671")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of Bot ]

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1002309567480').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @CINEMACCBOTUPDATES</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Verify
VERIFY = bool(environ.get('VERIFY', False)) # Verification On ( True ) / Off ( False )
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/DownloadYourLink/11') # How to open tutorial link for verification

# Others
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
BOT_USERNAME = environ.get("BOT_USERNAME", "GGV1_PROBOT")
BOT_NAME = environ.get("BOT_NAME", "GG V1")
BOT_ID = environ.get("BOT_ID", "7963564956")
S_GROUP = environ.get('S_GROUP', "CINEMACCBOTDISCUSSION")
S_CHANNEL = environ.get('S_CHANNEL', "CINEMACCBOTUPDATES")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/DARKSARVAR1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/MOVIECHANNEL_LINKCC')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/DownloadYourLink/11') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
MSG_ALRT = environ.get('MSG_ALRT', 'ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : GG ʙᴏᴛs')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002451523671') #Log channel id ( make sure bot is admin )
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/CINEMACCBOTDISCUSSION') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]


# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002451523671'))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
