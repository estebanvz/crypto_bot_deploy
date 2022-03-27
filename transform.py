import pandas as pd
import yaml
from sklearn.preprocessing import MinMaxScaler

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


def transform_dataset(cripto):
    dataset = pd.read_csv(
        f"{FOLDER}/{TIME_INTERVAL}/{cripto}.csv".format(cripto), sep="|"
    )
    dataset = dataset.set_index("Index")
    del dataset["Date"]
    dataset = dataset
    scaler = MinMaxScaler(feature_range=[-30, 30])
    dataset["lr"] = scaler.fit_transform(dataset["lr"].values.reshape(-1, 1))
    return dataset