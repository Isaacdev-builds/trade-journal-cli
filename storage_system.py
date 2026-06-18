import json
import os

def save_trades(trades):
    with open("trades.json", "w") as file:
        json.dump(trades, file, indent=4)

    print("Trades saved successfully.")


def load_trades():
    if not os.path.exists("trades.json"):
        return []

    with open("trades.json", "r") as file:
        trades = json.load(file)

    return trades