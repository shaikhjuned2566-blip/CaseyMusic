# 🎵 CaseyMusic - Modern Telegram Music Bot

A powerful, high-performance Telegram Music and Video Streaming Bot written in Python using Pyrogram and Py-Tgcalls. Built with integrated HTTP health-check server for seamless 24/7 deployment on **Render**, **Railway**, **Heroku**, and **VPS**.

---

## 🌟 Key Features

- 🎧 **High Quality Audio & Video Streaming**: Smooth voice chat streaming with video support.
- ⚡ **Multi-Platform Support**: Stream tracks from YouTube, Spotify, Apple Music, Resso, SoundCloud, and direct Telegram audio/video files.
- 🌐 **Render & Railway Ready**: Includes built-in `aiohttp` web server bound to `$PORT` to pass platform health checks automatically without port-scan timeouts or crash loops.
- 🛠️ **Bug-Fixed & Modernized**: Compatible with Python 3.10+ and standard library `asyncio`; updated `yt-dlp` for uninterrupted YouTube downloads.
- 🎛️ **Rich Admin & User Tools**: Speed controls, queue management, volume adjustments, lyrics search, and auto-clean mode.

---

## 🚀 Hosting & Deployment Guides

### 1. 🚀 Deploy on Render (Recommended Free/Paid Hosting)

Render provides easy cloud hosting. Follow these steps to deploy **CaseyMusic**:

[![Deploy to Render](https://render.com/images/deploy-to-render.svg)](https://render.com)

#### Step-by-Step Instructions:
1. **Fork or Push** this repository (`CaseyMusic`) to your GitHub account.
2. Sign in to [Render.com](https://dashboard.render.com/).
3. Click **New +** -> **Web Service** (or **Blueprint**).
4. Connect your GitHub repository `CaseyMusic`.
5. Set the build parameters:
   - **Environment**: `Docker` (or `Python 3`)
   - **Build Command**: `pip install -r requirements.txt` (or leave default for Docker)
   - **Start Command**: `bash start`
6. Under **Environment Variables**, add all required keys (see table below):
   - `API_ID`
   - `API_HASH`
   - `BOT_TOKEN`
   - `MONGO_DB_URI`
   - `OWNER_ID`
   - `LOGGER_ID`
   - `STRING_SESSION`
   - `PORT`: `8080` (or `10000`)
7. Click **Deploy Web Service**. Render will build and launch your bot automatically!

---

### 2. 🚆 Deploy on Railway

Railway allows fast, reliable hosting with automatic Docker detection.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/)

#### Step-by-Step Instructions:
1. Sign in to [Railway.app](https://railway.app/).
2. Click **New Project** -> **Deploy from GitHub repo**.
3. Select your `CaseyMusic` repository.
4. Click **Add Variables** and insert your environment variables (refer to table below).
5. Railway automatically reads `railway.json` and `Dockerfile`, binds `$PORT`, and starts your bot seamlessly!

---

### 3. 💻 VPS / Local Machine Deployment

#### Prerequisites:
- Python 3.10 or higher
- Node.js & FFmpeg installed on system

#### Setup Commands:

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/CaseyMusic.git
cd CaseyMusic

# Install dependencies
pip3 install -U -r requirements.txt

# Create .env configuration file
cp sample.env .env
# Edit .env file with your API details using nano or vi
nano .env

# Run the bot
bash start
```

---

## 🔑 Environment Variables Reference

| Variable Name | Required | Description | Example |
|---|---|---|---|
| `API_ID` | **Yes** | Telegram API ID from [my.telegram.org](https://my.telegram.org) | `1234567` |
| `API_HASH` | **Yes** | Telegram API Hash from [my.telegram.org](https://my.telegram.org) | `a1b2c3d4e5f6...` |
| `BOT_TOKEN` | **Yes** | Telegram Bot Token from [@BotFather](https://t.me/BotFather) | `123456:ABC-DEF...` |
| `MONGO_DB_URI` | **Yes** | MongoDB Connection URL from [cloud.mongodb.com](https://cloud.mongodb.com) | `mongodb+srv://...` |
| `OWNER_ID` | **Yes** | Your numeric Telegram User ID | `6922271843` |
| `LOGGER_ID` | **Yes** | Telegram Group ID for logs (Must start with `-100`) | `-1001929735324` |
| `STRING_SESSION` | **Yes** | Pyrogram v2 String Session for Assistant Account | `BQBx...` |
| `PORT` | Optional | Port for health check web server (Default: `8080`) | `8080` |
| `BOT_NAME` | Optional | Name of your music bot | `CaseyMusic` |

---

## 🛠️ Generating Pyrogram v2 String Session

1. Open Telegram and search for [@StringFatherBot](https://t.me/StringFatherBot) or run a Pyrogram session generator script.
2. Select **Pyrogram v2**.
3. Enter your `API_ID` and `API_HASH`.
4. Enter your phone number and OTP to receive your `STRING_SESSION`.
5. Copy and paste the string into your `STRING_SESSION` variable on Render/Railway/.env.

---

## 📌 Useful Bot Commands

- `/play <song name/link>` - Play audio in Group Voice Chat
- `/vplay <song name/link>` - Play video in Group Voice Chat
- `/pause` - Pause current playback
- `/resume` - Resume paused playback
- `/skip` - Skip to next song in queue
- `/end` or `/stop` - Stop playback and leave voice chat
- `/queue` - View active song queue
- `/ping` - Check bot latency and server status

---

## 📄 License & Credits

- Built upon Pyrogram & Py-Tgcalls framework.
- Maintained & Enhanced as **CaseyMusic**.
