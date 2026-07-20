import json
import os

def save_trades(trades):
    with open("trades.json", "w", encoding="utf-8") as file:
        json.dump(trades, file, indent=4)
        
def load_trades():
    if not os.path.exists("trades.json"):
        return []

    try:
        with open("trades.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Warning: trades.json could not be read. Starting with an empty journal.")
        return []