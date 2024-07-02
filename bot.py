import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext, CallbackQueryHandler
from telegram.ext import Updater 
from telegram.error import BadRequest, NetworkError, TelegramError
from telegram.constants import ParseMode
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

async def start(update, context):
    await update.message.reply_text(await main_menu_message(), reply_markup=await main_menu_keyboard(), parse_mode=ParseMode.MARKDOWN_V2)

async def main_menu(update, context):
    query = update.callback_query
    await query.answer()
    try:
        await query.edit_message_text(
            text=await main_menu_message(),
            reply_markup=await main_menu_keyboard()
        )
    except NetworkError as e:
        logging.warning(f"Network error occurred while sending message: {e}")
    except BadRequest as e:
        if str(e) != "Message is not modified: specified new message content and reply markup are exactly the same as a current content and reply markup of the message":
            logging.error(f"Bad request error occurred: {e}")
            # other bad request errors
        else:
            logging.info("Message content and reply markup are the same; no changes made.")
    except TelegramError as e:
        logging.error(f"Telegram error occurred: {e}")
        # other Telegram errors
    except Exception as e:
        logging.exception(f"An unexpected error occurred while sending message: {e}")

async def first_menu(update, context):
    query = update.callback_query
    await query.answer()
    try:
        await query.edit_message_text(
            text=await first_menu_message(),
            reply_markup=await first_menu_keyboard()
        )
    except NetworkError as e:
        logging.warning(f"Network error occurred while sending message: {e}")
    except BadRequest as e:
        if str(e) != "Message is not modified: specified new message content and reply markup are exactly the same as a current content and reply markup of the message":
            logging.error(f"Bad request error occurred: {e}")
            # other bad request errors
        else:
            logging.info("Message content and reply markup are the same; no changes made.")
    except TelegramError as e:
        logging.error(f"Telegram error occurred: {e}")
        # other Telegram errors
    except Exception as e:
        logging.exception(f"An unexpected error occurred while sending message: {e}")

async def second_menu(update, context):
    query = update.callback_query
    await query.answer()
    try:
        await query.edit_message_text(
            text=await second_menu_message(),
            reply_markup=await second_menu_keyboard()
        )
    except NetworkError as e:
        logging.warning(f"Network error occurred while sending message: {e}")
    except BadRequest as e:
        if str(e) != "Message is not modified: specified new message content and reply markup are exactly the same as a current content and reply markup of the message":
            logging.error(f"Bad request error occurred: {e}")
            # other bad request errors
        else:
            logging.info("Message content and reply markup are the same; no changes made.")
    except TelegramError as e:
        logging.error(f"Telegram error occurred: {e}")
        # other Telegram errors
    except Exception as e:
        logging.exception(f"An unexpected error occurred while sending message: {e}")

async def third_menu(update, context):
    query = update.callback_query
    await query.answer()
    try:
        await query.edit_message_text(
            text=await third_menu_message(),
            reply_markup=await third_menu_keyboard()
        )
    except NetworkError as e:
        logging.warning(f"Network error occurred while sending message: {e}")
    except BadRequest as e:
        if str(e) != "Message is not modified: specified new message content and reply markup are exactly the same as a current content and reply markup of the message":
            logging.error(f"Bad request error occurred: {e}")
            # other bad request errors
        else:
            logging.info("Message content and reply markup are the same; no changes made.")
    except TelegramError as e:
        logging.error(f"Telegram error occurred: {e}")
        # other Telegram errors
    except Exception as e:
        logging.exception(f"An unexpected error occurred while sending message: {e}")

# and so on for every callback_data option
async def first_submenu(bot, update):
    pass

async def second_submenu(bot, update):
    pass

# menu keyboards
async def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('💰 Buy', callback_data='m1'),
                 InlineKeyboardButton('📤 Transfer', callback_data='m2')],
                [InlineKeyboardButton('🏹 Sniper', callback_data='full_feature'),
                 InlineKeyboardButton('💰 Positions', callback_data='full_feature')],
                [InlineKeyboardButton('🤑 Refer', callback_data='full_feature'),
                 InlineKeyboardButton('🔠 Language', callback_data='full_feature')],
                [InlineKeyboardButton('⚙️ Settings', callback_data='full_feature')]]
    return InlineKeyboardMarkup(keyboard)

async def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

async def second_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

async def third_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Submenu 3-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 3-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

# commands / menu messages
async def main_menu_message(): 
    return 'Safepile Bot Demo \\(*v1\\.0*\\) \n\nSuch description, much wow\\! \n~                                                             ~ \n\n[Dev](tg://user?id=0081120000)'

async def first_menu_message():
    return 'SPT ➡️⬅️ ETH'

async def second_menu_message():
    return 'Choose the submenu in second menu:'

async def third_menu_message():
    return 'Choose the submenu in second menu:'

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
    # await query.answer()

    # Logging the callback data for debugging
    logger.info(f"Callback data: {query.data}")

    # Handle callback data for buttons
    if query.data == 'full_feature':
        await query.answer(text="This feature is available in the full version of the bot.", show_alert=True)
        logger.info("Showing alert for full feature")
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

    # menu startoff
    # application.add_handler(CallbackQueryHandler(button))

    # full features
    application.add_handler(CallbackQueryHandler(full_button_callback))

    # unrecognized commands
    application.add_handler(MessageHandler(filters.COMMAND, unrecognized_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
