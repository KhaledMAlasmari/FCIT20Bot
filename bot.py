#!/usr/bin/env python
# This program is dedicated to the public domain under the CC0 license.
# pylint: disable=import-error,wrong-import-position
"""
Simple example of a bot that uses a custom webhook setup and handles custom updates.
For the custom webhook setup, the libraries `starlette` and `uvicorn` are used. Please install
them as `pip install starlette~=0.20.0 uvicorn~=0.17.0`.
Note that any other `asyncio` based web server framework can be used for a custom webhook setup
just as well.

Usage:
Set bot token, url, admin chat_id and port at the start of the `main` function.
You may also need to change the `listen` value in the uvicorn configuration to match your setup.
Press Ctrl-C on the command line or send a signal to the process to stop the bot.
"""
import asyncio
import logging
from dataclasses import dataclass
from http import HTTPStatus
import os

import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from starlette.routing import Route

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackContext,
    MessageHandler,
    filters,
    ContextTypes,
    ExtBot,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


@dataclass
class WebhookUpdate:
    """Simple dataclass to wrap a custom update type"""

    user_id: int
    payload: str


class CustomContext(CallbackContext[ExtBot, dict, dict, dict]):
    """
    Custom CallbackContext class that makes `user_data` available for updates of type
    `WebhookUpdate`.
    """

    @classmethod
    def from_update(
        cls,
        update: object,
        application: "Application",
    ) -> "CustomContext":
        if isinstance(update, WebhookUpdate):
            return cls(application=application, user_id=update.user_id)
        return super().from_update(update, application)


async def driveFolders(update: Update, context):
    await update.message.reply_text(text="""درايفات الطلاب: \n
	<a href='https://drive.google.com/drive/folders/1eCO7-OEzR0MxdDmIWmRMmA4m4r6FzL8q'>دفعة 16</a> \n
	<a href='https://drive.google.com/drive/folders/1x2HaC3PF0ExBtw62AZ4uYmUPCUpiCEoK'>دفعة 17</a> \n
	<a href='http://fcit18.link/'>دفعة 18</a> \n
	<a href='https://drive.google.com/drive/u/0/folders/1v_CJph-q7Y6YmHgVC3eRR7lC6L4Rfaai'>دفعة 19</a> \n
	<a href='https://drive.google.com/drive/folders/19e5ISP2SixVw3if__J6ILxCo9ZrojH-Y'>دفعة 20 (مافيا)</a> \n
	<a href='https://drive.google.com/drive/u/2/folders/1vEI6drswcgZeRipqURtUQMh-jFUqBnXt'>دفعة 21</a> \n
	درايفات الطالبات: \n
	<a href='https://cutt.ly/RyXrwgs'>دفعة 18</a> \n
	<a href='https://bit.ly/2KZBuxG'>دفعة 19</a> \n
	<a href='https://drive.google.com/drive/folders/1mQkfU0QZKvUzueZaEiw6OZTH2ApXJiPB'>دفعة 20</a> \n
	<a href='https://drive.google.com/drive/u/0/folders/1mPQNueRjBXexBYAZVJWCKSc_7osuQMHw?lfhs=2'>دفعة 20 - تسجيلات الدكاترة</a> \n
	<a href='https://drive.google.com/drive/folders/1Yg7EDNRkTA4QLG71lgnriwt2jD-e2zeW'>دفعة 21</a> \n""",parse_mode=ParseMode.HTML)


async def channels(update: Update, context):
    await update.message.reply_text(text="""القنوات المتاحة: \n
    <a href='https://t.me/FCIT20_CS'>قنوات علوم الحاسبات</a> \n
    <a href='https://t.me/FCIT20_IT'>قنوات تقنية المعلومات</a> \n
    <a href='https://t.me/FCIT20_IS_1'>قنوات نظم المعلومات</a> \n
    <a href='https://t.me/FCIT20_Shared'>قنوات المواد المشتركة</a> \n
    <a href='https://t.me/FcitBank'>بنك المعلومات الطلابي FCIT</a> \n
    <a href='https://t.me/FCIT20Male'>قروب MAFIA 20 ، (مناقشة أو إستفسار تعال هنا):</a> \n""",parse_mode=ParseMode.HTML)

async def avaliableCommands(update: Update, context):
    await update.message.reply_text("""الأوامر المتاحة: \n
    1- درايف \n
    2- قنوات \n
    3- بوت20 \n
    4- discord""")


async def discordServer(update: Update, context):
    await update.message.reply_text("<a href='https://discord.com/invite/9wyYEY9gcg'>Programmers of KAU</a>", parse_mode= ParseMode.HTML)





async def main() -> None:
    """Set up the application and a custom webserver."""
    port = int(os.environ.get('PORT', 5000))
    token = os.environ.get('TOKEN')
    url = os.environ.get('WEBHOOK_URL')
    admin_chat_id = os.environ.get('admin_chat_id')


    
    context_types = ContextTypes(context=CustomContext)
    # Here we set updater to None because we want our custom webhook server to handle the updates
    # and hence we don't need an Updater instance
    application = (
        Application.builder().token(token).updater(None).context_types(context_types).build()
    )
    # save the values in `bot_data` such that we may easily access them in the callbacks
    application.bot_data["url"] = url
    application.bot_data["admin_chat_id"] = admin_chat_id

    # register handlers
    #application.add_handler(CommandHandler("start", start))
    #application.add_handler(TypeHandler(type=WebhookUpdate, callback=webhook_update))
    
    application.add_handler(MessageHandler(filters.Text(["درايف"]), driveFolders))
    application.add_handler(MessageHandler(filters.Text(["قنوات"]), channels))
    application.add_handler(MessageHandler(filters.Text(["بوت20"]), avaliableCommands))
    application.add_handler(MessageHandler(filters.Text(["discord"]), discordServer))
    # Pass webhook settings to telegram
    await application.bot.set_webhook(url=f"{url}/telegram")

    # Set up webserver
    async def telegram(request: Request) -> Response:
        """Handle incoming Telegram updates by putting them into the `update_queue`"""
        await application.update_queue.put(
            Update.de_json(data=await request.json(), bot=application.bot)
        )
        
        return Response()

    async def health(_: Request) -> PlainTextResponse:
        """For the health endpoint, reply with a simple plain text message."""
        return PlainTextResponse(content="The bot is still running fine :)")

    starlette_app = Starlette(
        routes=[
            Route("/telegram", telegram, methods=["POST"]),
            Route("/healthcheck", health, methods=["GET"]),
        ]
    )
    webserver = uvicorn.Server(
        config=uvicorn.Config(
            app=starlette_app,
            port=port,
            use_colors=False,
            host="0.0.0.0",
        )
    )

    # Run application and webserver together
    async with application:
        await application.start()
        await webserver.serve()
        await application.stop()


if __name__ == "__main__":
    asyncio.run(main())