import os
import asyncio
from aiohttp import web
from ..logging import LOGGER

async def health_check(request):
    return web.Response(
        text="<html><body><h1>CaseyMusic Bot is Online & Running!</h1></body></html>",
        content_type="text/html",
        status=200
    )

async def start_web_server():
    port = int(os.getenv("PORT", 8080))
    app = web.Application()
    app.router.add_get("/", health_check)
    app.router.add_get("/health", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    try:
        await site.start()
        LOGGER("AnonXMusic.server").info(f"✦ Web Server started on port {port} (0.0.0.0:{port})")
    except Exception as e:
        LOGGER("AnonXMusic.server").error(f"✦ Failed to start Web Server on port {port}: {e}")
