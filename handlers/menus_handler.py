import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import Updater
from telegram.error import BadRequest, NetworkError, TelegramError

async def main_menu_message(): 
    return 'Safepile Bot Demo \\(*v1\\.0*\\) \n\nSuch description, much wow\\! \n~                                                             ~ \n\n[Dev](tg://user?id=0081120000)'

async def first_menu_message():
    return 'SPT ➡️⬅️ ETH'

async def second_menu_message():
    return 'Choose the submenu in second menu:'

async def third_menu_message():
    return 'Choose the submenu in second menu:'

async def main_menu(update, context):
    query = update.callback_query
    await query.answer()
    try:
        await query.edit_message_text(
            text=await main_menu_message(),
            reply_markup=await main_menu_keyboard(),
            parse_mode=ParseMode.MARKDOWN_V2
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
            reply_markup=await first_menu_keyboard(),
            parse_mode=ParseMode.MARKDOWN_V2
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
            reply_markup=await second_menu_keyboard(),
            parse_mode=ParseMode.MARKDOWN_V2
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
            reply_markup=await third_menu_keyboard(),
            parse_mode=ParseMode.MARKDOWN_V2
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