# %%
import os

import yaml
from telegram import ChatAction
from telegram.ext import CommandHandler, Updater

from extract import extract_data
from load import build_img
from transform import transform_dataset
from prediction import simple_prediction
from dotenv import load_dotenv

load_dotenv()

CRYPTOS = [
    "BTCUSDT",
]
TIME_INTERVAL = "1d"
TIME_HOURS = 2400
FOLDER = "./datasets"
TOKEN = os.environ["TELEGRAM_TOKEN"]
PASS = os.environ["PASS"]

with open(r"config.yml") as file:
    config = yaml.full_load(file)
    CRYPTOS = config["CRYPTOS"]
    TIME_INTERVAL = config["TIME_INTERVAL"]
    TIME_HOURS = config["TIME_HOURS"]
    FOLDER = config["FOLDER"]

def price_consult(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Please select a crypto like BTCUSDT")
        return

    cripto = str(context.args[0]).upper()

    if "USDT" not in cripto:
        cripto = cripto + "USDT"

    if cripto not in CRYPTOS:
        update.message.reply_text("This crypto {} is not in my database".format(cripto))
        return


    dataset = transform_dataset(cripto)
    prediction = simple_prediction(dataset)
    img_path = build_img(dataset, cripto)

    chat = update.message.chat
    chat.send_action(action=ChatAction.UPLOAD_PHOTO, timeout=None)
    chat.send_photo(photo=open(img_path, "rb"))
    update.message.reply_text(
        "Analizando {}. Precio actual: {} ".format(cripto, dataset["Close"][-1])
    )
    update.message.reply_text(
        "\n".join(prediction)
    )


def update_prices(update, context):
    if len(context.args) == 0:
        return
    else:
        if context.args[0] is not PASS:
            return
    update.message.reply_text(" Downloading data...")
    extract_data()
    update.message.reply_text(" Bot updated!")


def welcome(update, context):
    update.message.reply_text(
        " Welcome to e-cryptobot! The most reliable clever trader bot in the market! "
    )


updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("welcome", welcome))  # /welcome
dp.add_handler(CommandHandler("crypto", price_consult))  # /crypto BTCUSDT
dp.add_handler(CommandHandler("c", price_consult))  # /crypto BTCUSDT
dp.add_handler(CommandHandler("update", update_prices))  # /crypto BTCUSDT
updater.start_polling()
updater.idle()
# %%
