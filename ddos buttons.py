import nest_asyncio
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Set to store user IDs
user_ids = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_ids.add(update.effective_user.id)  # Add user ID to the set
    button1 = KeyboardButton("")
    button2 = KeyboardButton("")
    button3 = KeyboardButton("/bgmi")
    button4 = KeyboardButton("/time")
    keyboard = [[button1, button2], [button3, button4]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text("@ILLEGALCHEAT78 DM TO BUY ACCESS", reply_markup=reply_markup)

async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    if user_message == "/attack":
        await update.message.reply_text("WAIT KAR BSDK.")
    elif user_message == "/when":
        await update.message.reply_text("RUK JA LOUDA.")
    elif user_message == "/info":
        await update.message.reply_text("Yeh bot aapki madad ke liye hai.")
    elif user_message == "/help":
        await update.message.reply_text("Aapko kya madad chahiye? Aap /attack ya /when ka istemal kar sakte hain.")
    else:
        await update.message.reply_text("")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id != 1938125200:  # Replace with your Telegram user ID
        await update.message.reply_text("You are not authorized to use this command.")
        return

    message = ' '.join(context.args)
    if not message:
        await update.message.reply_text("Please provide a message to broadcast.")
        return

    for user_id in user_ids:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"Failed to send message to {user_id}: {e}")

    await update.message.reply_text("Broadcast message sent.")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == '/attack':
        await query.edit_message_text(text="You selected Option 1 from inline buttons.")
    elif query.data == '/when':
        await query.edit_message_text(text="You selected Option 2 from inline buttons.")

async def main() -> None:
    token = '7831188701:AAFdxZhKGPAXXwysFyGsTrysHHtJ9gItjOw'  # Replace with your actual token
    application = ApplicationBuilder().token(token).build()

    # Command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Command handler for /broadcast
    application.add_handler(CommandHandler("broadcast", broadcast))

    # Message handler for reply keyboard options
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))

    # Callback query handler for inline buttons
    application.add_handler(CallbackQueryHandler(button))

    await application.run_polling()

if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())
        except Exception as e:
            print(f"Bot crashed with error: {e}")
            print("Restarting in 10 seconds...")
            asyncio.sleep(10)