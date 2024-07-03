import logging
import config

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext, CallbackQueryHandler
from telegram.ext import Updater
from telegram.constants import ParseMode
from handlers.start_handler import start
from handlers.wallet_handler import generate_wallet
from handlers.menus_handler import main_menu, first_menu, second_menu, third_menu, first_submenu, second_submenu, main_menu_message, main_menu_keyboard

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def start(update, context):
    await update.message.reply_text(await main_menu_message(), reply_markup=await main_menu_keyboard(), parse_mode=ParseMode.MARKDOWN_V2)

# commands
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def unrecognized_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("⚠️ Sorry, I don't understand that command. Type /start to access my main menu.")

async def full_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query.data == 'full_feature':
        await query.answer(text="This feature is available in the full version of the bot.", show_alert=True)
    else:
        await query.answer()

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()

    # commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("generate_wallet", generate_wallet))

    # menu
    application.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    application.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    application.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    application.add_handler(CallbackQueryHandler(third_menu, pattern='m3'))\

    application.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
    application.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))

    # full features only
    application.add_handler(CallbackQueryHandler(full_button_callback))

    # unrecognized commands
    application.add_handler(MessageHandler(filters.COMMAND, unrecognized_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
