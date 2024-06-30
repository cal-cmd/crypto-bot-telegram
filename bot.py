import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import config
from handlers.start_handler import start
from handlers.wallet_handler import generate_wallet

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()

    option = query.data

    if option == "1":
        await CommandHandler("generate_wallet", generate_wallet).callback(update, context)
    elif option == "2":
        await context.bot.send_message(chat_id=query.message.chat_id, text="Running /command2")
    elif option == "3":
        await context.bot.send_message(chat_id=query.message.chat_id, text="Running /command3")
    else:
        await query.edit_message_text(text=f"Selected option: {option}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def unrecognized_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("⚠️ Sorry, I don't understand that command. Type /help for available commands.")

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()

    # commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("generate_wallet", generate_wallet))

    # menu startoff
    application.add_handler(CallbackQueryHandler(button))

    # unrecognized commands
    application.add_handler(MessageHandler(filters.COMMAND, unrecognized_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
