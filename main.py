import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import config
from rate import Currate

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Добрый день. Как вас зовут?")

async def handler_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    responce = (await Currate(config.API_KEY).get_currency())
    rubles = round(responce.get('data').get('RUB').get('value'), 2)
    context.user_data["name"] = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Рад знакомству, {context.user_data["name"]}! Курс доллара сегодня {rubles}р')

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.TOKEN).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler_message))
    application.run_polling()

