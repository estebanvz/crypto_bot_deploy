import pandas as pd
import yaml
CRYPTOS = [
    "BTCUSDT",
]
cripto=CRYPTOS[0]
TIME_INTERVAL = "1d"
TIME_HOURS = 2400
FOLDER = "./datasets"

with open(r"config.yml") as file:
    config = yaml.full_load(file)
    CRYPTOS = config["CRYPTOS"]
    TIME_INTERVAL = config["TIME_INTERVAL"]
    TIME_HOURS = config["TIME_HOURS"]
    FOLDER = config["FOLDER"]

def evaluate_short(adx,lr,mdm,pdm):
    result=[]
    points=0
    if(adx[-1]>23):
        if(pdm<mdm):
            points+=2
            result.append(["El modelo presenta un adx negativo con fuerza!!"])
    if(lr[-2]>lr[-1]):
        points+=1
        result.append(["La regresión lineal es negativa!"])
    if(lr[-1]>0):
        points+=1
        result.append(["La regresión lineal esta en la parte de arriba!"])
    if(points>2):
        return result
    else:
        return ["Se recomienda no operar"]
def evaluate_long(adx,lr,mdm,pdm):
    result=[]
    points=0
    if(adx[-1]>23):
        if(pdm>mdm):
            points+=2
            result.append(["El modelo presenta un adx positivo con fuerza!!"])
    if(lr[-2]>lr[-1]):
        points+=1
        result.append(["La regresión lineal es positiva!"])
    if(lr[-1]>0):
        points+=1
        result.append(["La regresión lineal esta en la parte de abajo!"])
    if(points>2):
        return result
    else:
        return ["Se recomienda no operar"]
def simple_prediction(dataset):
    last=dataset[-1:]
    if(last["55"].values>last["Open"].values):
        return evaluate_short(dataset["adx"][-2:].values,dataset["lr"][-2:].values,dataset["mdm"][-1:].values,dataset["pdm"][-1:].values)
    else:
        return evaluate_long(dataset["adx"][-2:].values,dataset["lr"][-2:].values,dataset["mdm"][-1:].values,dataset["pdm"][-1:].values)
if(__name__=="__main__"):
    dataset = pd.read_csv(
        f"{FOLDER}/{TIME_INTERVAL}/{cripto}.csv".format(cripto), sep="|"
    )

    simple_prediction(dataset)