import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import os

## deployed on heroku. Please add env variables in there!
PORT = int(os.environ.get('PORT', 5000))

TOKEN = os.environ.get('TOKEN')
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')

def driveFolders(update, context):
    update.message.reply_text(text="""درايفات الطلاب: \n
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
	<a href='https://drive.google.com/drive/folders/1Yg7EDNRkTA4QLG71lgnriwt2jD-e2zeW'>دفعة 21</a> \n\n""",parse_mode=ParseMode.HTML)
def channels(update, context):
    update.message.reply_text(text="""القنوات المتاحة: \n
    <a href='https://t.me/FCIT20_CS'>قنوات علوم الحاسبات</a> \n
    <a href='https://t.me/FCIT20_IT'>قنوات تقنية المعلومات</a> \n
    <a href='https://t.me/FCIT20_IS_1'>قنوات نظم المعلومات</a> \n
    <a href='https://t.me/FCIT20_Shared'>قنوات المواد المشتركة</a> \n
    <a href='https://t.me/FcitBank'>بنك المعلومات الطلابي FCIT</a> \n
    <a href='https://t.me/FCIT20Male'>قروب MAFIA 20 ، (مناقشة أو إستفسار تعال هنا):</a> \n""",parse_mode=ParseMode.HTML)
    update.message.reply_text(text="",parse_mode=ParseMode.HTML)

def avaliableCommands(update, context):
    update.message.reply_text("""الأوامر المتاحة: \n
    1- درايف \n
    2- قنوات \n
    3- بوت20 \n
    4- discord""")
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
    dp.add_handler(MessageHandler(Filters.text(["discord"]), discordServer))

    updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=TOKEN)
    updater.bot.setWebhook(f'{WEBHOOK_URL}/{TOKEN}')

    updater.idle()

if __name__ == '__main__':
    main()
