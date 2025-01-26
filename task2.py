import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from transformers import pipeline

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load LLM pipeline
# Replace with TinyLlama or another model if required
llm = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# Define Telegram bot commands and handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am your AI Assistant. How can I help you today?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.strip()
    logging.info(f"Received message: {user_message}")

    prompt = f"Explain in detail about {user_message.lower()}."

    try:

        response = llm(prompt, max_length=300, min_length=50, temperature=0.3, top_p=0.9, repetition_penalty=2.5, num_return_sequences=1, truncation=True)
        # reply = response[0]['generated_text']
        print(f"Model raw output: {response}")

        reply = response[0]['generated_text']
    except Exception as e:
        logging.error(f"Error during LLM inference: {e}")
        reply = "Sorry, something went wrong while processing your request."

    if not reply.strip():
        reply = "I'm sorry, I couldn't find detailed information about that. Can you try asking differently?"

    await update.message.reply_text(reply)


# Main function
if __name__ == "__main__":
    # Replace 'YOUR_API_TOKEN' with the API token from BotFather
    application = ApplicationBuilder().token("8141755374:AAGAoTekr3aKDG1kAvPi9S7bFsVhdEDJAlA").build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))

    # Message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()
