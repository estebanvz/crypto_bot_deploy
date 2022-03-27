import os

import yaml
from crypto_metrics import CryptoDataTransformation
from crypto_price import CryptoDataExtractor
from dotenv import load_dotenv

load_dotenv()
CRYPTOS = [
    "BTCUSDT",
]
TIME_INTERVAL = "1d"
TIME_HOURS = 2400
FOLDER = "./datasets"

with open(r"config.yml") as file:
    config = yaml.full_load(file)
    CRYPTOS = config["CRYPTOS"]
    TIME_INTERVAL = config["TIME_INTERVAL"]
    TIME_HOURS = config["TIME_HOURS"]
    FOLDER = config["FOLDER"]


def extract_data():
    API_KEY = os.environ["API_KEY"]
    API_SECRET = os.environ["API_SECRET"]

    extractor = CryptoDataExtractor(save_path=FOLDER, criptos=CRYPTOS)
    extractor.from_binance(
        api_key=API_KEY,
        api_secret=API_SECRET,
        time_in_hours=TIME_HOURS,
        time_interval=TIME_INTERVAL,
    )
    transformer = CryptoDataTransformation(
        save_path=f"{FOLDER}/{TIME_INTERVAL}", criptos=CRYPTOS
    )
    transformer.readDataset()
if __name__=="__main__":
    extract_data()