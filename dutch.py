from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder

TOKEN = '8737393959:AAGfNXQAKc6SEemkh07KfBASY2SbIVv5Pek'
CHAT_ID = '@REDDEAD19'
RULES_CHANNEL_LINK = 'https://t.me/REDDEAD19/9'
MESSAGE_TEXT = '⚠️ تنبيه: يرجى الاطلاع على القوانين والالتزام بها لتجنب المخالفات.'

async def send_message(context):
    keyboard = [[InlineKeyboardButton("📜 القوانين 📜📝", url=RULES_CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=CHAT_ID, text=MESSAGE_TEXT, reply_markup=reply_markup)

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    job_queue = application.job_queue
    job_queue.run_repeating(send_message, interval=1800, first=10)
    application.run_polling()

if __name__ == '__main__':
    main()
