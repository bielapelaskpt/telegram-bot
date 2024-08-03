import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Eu sou seu bot.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Certifique-se de que a variável de ambiente está corretamente configurada
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("No token found. Please set the TELEGRAM_BOT_TOKEN environment variable.")
    
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == '__main__':
    main()
