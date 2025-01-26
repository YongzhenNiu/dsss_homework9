from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes


API_TOKEN = "8141755374:AAGAoTekr3aKDG1kAvPi9S7bFsVhdEDJAlA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("Hello! I am your AI assistant. How can I help you?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text
    print(f"Received message: {user_message}")
    await update.message.reply_text(f"You said: {user_message}")

def main():

    application = ApplicationBuilder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
