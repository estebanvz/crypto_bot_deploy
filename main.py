#%%
import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.environ["TELEGRAM_TOKEN"]
def welcome(update, context):
    update.message.reply_text(
        " Welcome to e-cryptobot! The most reliable clever trader bot in the market! "
    )
if __name__ == '__main__':
    updater = Updater(
        token = TOKEN, use_context=True
    )
    dp = updater.dispatcher
    dp.add_handler( CommandHandler('welcome', welcome) )
    updater.start_polling()
    updater.idle()
# %%
