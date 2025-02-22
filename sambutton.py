from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackContext

# Bot Token
TOKEN = '7831188701:AAFdxZhKGPAXXwysFyGsTrysHHtJ9gItjOw'  # Replace with your actual bot token

# Command to start the bot and show the /bgmi and /time buttons
async def start(update: Update, context: CallbackContext):
    # Defining the /bgmi and /time buttons for the reply keyboard
    keyboard = [
        [KeyboardButton("/bgmi")],
        [KeyboardButton("/time")]
    ]
    
    # Create a reply markup to attach the keyboard to the message
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Send a message with the reply keyboard
    await update.message.reply_text('Click a button below:', reply_markup=reply_markup)

# Handle /bgmi button click (do nothing, no response)
async def attack(update: Update, context: CallbackContext):
    # Do nothing when /bgmi button is pressed
    pass  # No response

# Handle /time button click (do nothing, no response)
async def when(update: Update, context: CallbackContext):
    # Do nothing when /time button is pressed
    pass  # No response

# Main function to start the bot
def main():
    application = Application.builder().token(TOKEN).build()

    # Command handler for /start command
    application.add_handler(CommandHandler('start', start))

    # Command handler for /bgmi and /time (no response for both)
    application.add_handler(CommandHandler('attack', attack))
    application.add_handler(CommandHandler('when', when))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
