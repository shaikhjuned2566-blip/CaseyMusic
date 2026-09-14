import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# --- Telegram API Credentials ---
API_ID = int(getenv("API_ID")) if getenv("API_ID") else None
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)

# --- Bot & Assistant Details ---
BOT_USERNAME = getenv("BOT_USERNAME", None)
BOT_NAME = getenv("BOT_NAME", "Music Bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", None)
ASSUSERNAME = getenv("ASSUSERNAME", None)

# --- IDs (Bot Owner & Log Group) ---
OWNER_ID = int(getenv("OWNER_ID")) if getenv("OWNER_ID") else None
LOGGER_ID = int(getenv("LOGGER_ID")) if getenv("LOGGER_ID") else None

# --- Database ---
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# --- Sessions ---
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# --- Spotify Credentials ---
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# --- Git & Upstream ---
UPSTREAM_REPO = getenv("UPSTREAM_REPO", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# --- Heroku (Optional) ---
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# --- Support & Community ---
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", None)

# --- Runtime Settings ---
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False").lower() in ("true", "1", "t")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# --- Internal States ---
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# --- Default UI Assets ---
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/dec61e858d57c14343455.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/7795e58425337d0455e95.jpg"
STATS_IMG_URL = "https://graph.org/file/27c86aaad1711abe65ce1.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# --- URL Validation ---
if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
