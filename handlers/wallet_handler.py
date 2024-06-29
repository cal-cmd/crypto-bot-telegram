# handlers/wallet_handler.py
from telegram import Update
from telegram.ext import ContextTypes
from scripts.generate_wallet import create_wallet

async def generate_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    wallet = create_wallet()
    await update.message.reply_text(
        f'Your new wallet address is:\n{wallet["address"]}\n\nYour private key is:\n{wallet["private_key"]}'
    )