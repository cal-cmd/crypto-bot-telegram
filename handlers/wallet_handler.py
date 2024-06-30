# handlers/wallet_handler.py
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from scripts.wallet import create_wallet

# generate wallet (add check for if user already has wallet, make them confirm before regenerating)
async def generate_wallet(update: Update, context: CallbackContext) -> None:
    if update.message:  # Check if update contains a message
        wallet = create_wallet()
        await update.message.reply_text(
            f'Your new wallet address is:\n{wallet["address"]}\n\nYour private key is:\n{wallet["private_key"]}'
        )
    elif update.callback_query:  # Handle callback queries from inline buttons
        wallet = create_wallet()
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text=f'Your new wallet address is:\n{wallet["address"]}\n\nYour private key is:\n{wallet["private_key"]}'
        )
    else:
        # Handle other types of updates
        pass

# save wallet info
def save_wallet_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler to save wallet information."""
    # Extract data from the generated wallet
    wallet_data = context.user_data.get('wallet_data')
    if wallet_data:
        # Save the wallet_data to users device or storage (implement this part)
        user_id = update.effective_user.id
        # Example: Store wallet_data in user's context (need to implement storage)
        context.user_data[user_id] = wallet_data
        update.message.reply_text("Wallet information saved.")