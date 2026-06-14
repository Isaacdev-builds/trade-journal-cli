def create_trade():

    pair = input("Pair: ").upper()
    direction = input("Direction (BUY/SELL): ").upper()
    risk = float(input("Risk Amount: $ "))
    rr = input("RR: ")
    result = input("Result (WIN/LOSS): ").upper()

    trade = {
        "pair": pair,
        "direction": direction,
        "risk": risk,
        "rr": rr,
        "result": result
    }

    return trade


def display_trades(trades):
    if len(trades) == 0:
        print("\nNo trades added yet.")
        return
    
    print("\n=== SAVED TRADES ===")

    for index, trade in enumerate(trades, start=1):
        print(f"\nTrade {index}:")
        print(f"Pair: {trade['pair']}")
        print(f"Direction: {trade['direction']}")
        print(f"Risk: ${trade['risk']:.2f}")
        print(f"RR: {trade['rr']}")
        print(f"Result: {trade['result']}")
        print("-" * 20)