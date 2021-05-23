import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import os

## deployed on heroku. Please add env variables in there!
PORT = int(os.environ.get('PORT', 5000))

TOKEN = os.environ.get('TOKEN')


def driveFolders(update, context):
    update.message.reply_text(text="""الدرايفات المتاحة: \n
    <a href='https://drive.google.com/drive/folders/19e5ISP2SixVw3if__J6ILxCo9ZrojH-Y'>درايف مافيا</a> \n
    <a href='https://drive.google.com/drive/u/0/folders/0B8oC3yMWyRu6SjRCek40Tmx3bDQ'>درايف علوم حاسب - 14</a> \n
    <a href='https://drive.google.com/drive/folders/0BxTTBNO16o2DVG5uQU96YzIzMDQ'>درايف علوم حاسب - 15</a> \n
    <a href='https://drive.google.com/drive/folders/1eCO7-OEzR0MxdDmIWmRMmA4m4r6FzL8q'>درايف علوم حاسب - 16</a> \n
    <a href='https://drive.google.com/drive/folders/1-6DWIYRVG-khvM_-tmLkU-hHjdPLgmmH'>درايف علوم حاسب - 17</a> \n
    <a href='https://drive.google.com/drive/folders/16EzY5HRid_UQMNgTT8tuXMD_ABYqxe45'>درايف دفعة 18</a> \n
    <a href='https://drive.google.com/drive/u/3/folders/1v_CJph-q7Y6YmHgVC3eRR7lC6L4Rfaai'>درايف دفعة 19</a> \n
    <a href='https://drive.google.com/drive/folders/0B9g1JPI3agkCZF96bWlsdndzNzg'>درايف علوم حاسب - دفعة (؟)</a> \n""",parse_mode=ParseMode.HTML)
def channels(update, context):
    update.message.reply_text(text="""القنوات المتاحة: \n
    <a href='https://t.me/FcitBank'>بنك المعلومات الطلابي FCIT</a> \n
    <a href='https://t.me/FCIT_20_CPCS_222'>تراكيب متقطعة - CPCS222</a> \n
    <a href='https://t.me/joinchat/URLJZcFv2svJcpF8'>برمجة 2 - CPCS203</a> \n
    <a href='https://t.me/FCIT20_CPCS204'>برمجة 3 - CPCS204</a> \n
    <a href='https://t.me/CPIT220'>مقدمة لتقنية المعلومات  -  CPIT220</a> \n
    <a href='https://t.me/AMath202'>تفاضل وتكامل 2 - MATH202</a> \n
    <a href='https://t.me/FCIT20Male'>قروب MAFIA 20 ، (مناقشة أو إستفسار تعال هنا):</a> \n""",parse_mode=ParseMode.HTML)
    update.message.reply_text(text="",parse_mode=ParseMode.HTML)

def avaliableCommands(update, context):
    update.message.reply_text("""الأوامر المتاحة: \n
    1- درايف \n
    2- قنوات \n
    3- بوت20 \n
    4- discord
    5- تواصل""")
def contactMe(update, context):
    update.message.reply_text("""للتواصل:\n
    <a href='https://twitter.com/KhaledMAlasmari'>تويتر</a> \n
    <a href='https://KhaledAlAsmari.com/'>موقعي</a> \n""", parse_mode= ParseMode.HTML)


def help(update, context):
    update.message.reply_text('Help!')


def discordServer(update, context):
     update.message.reply_text("<a href='https://discord.com/invite/9wyYEY9gcg'>Programmers of KAU</a>", parse_mode= ParseMode.HTML)

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text(["درايف"]), driveFolders))
    dp.add_handler(MessageHandler(Filters.text(["قنوات"]), channels))
    dp.add_handler(MessageHandler(Filters.text(["بوت20"]), avaliableCommands))
    dp.add_handler(MessageHandler(Filters.text(["تواصل"]), contactMe))
    dp.add_handler(MessageHandler(Filters.text(["discord"]), discordServer))

    updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=TOKEN)
    updater.bot.setWebhook('https://fcit20bot.herokuapp.com/' + TOKEN)

    updater.idle()

if __name__ == '__main__':
    main()
