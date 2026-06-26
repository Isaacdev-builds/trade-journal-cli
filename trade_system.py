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

def delete_trade(trades, trade_number):
    trade_index = trade_number - 1

    if trade_index < 0 or trade_index >= len(trades):
        print("Invalid trade number.")
        return

    deleted_trade = trades.pop(trade_index)

    print("Trade deleted:")
    print(f"Pair: {deleted_trade['pair']}")
    print(f"Direction: {deleted_trade['direction']}")
    print(f"Risk: ${deleted_trade['risk']:.2f}")
    print(f"RR: {deleted_trade['rr']}")
    print(f"Result: {deleted_trade['result']}")

def edit_trade(trades, trade_number):
    trade_index = trade_number - 1

    if trade_index < 0 or trade_index >= len(trades):
        print("Invalid trade number.")
        return

    print("\nEditing Trade")

    new_risk = float(input("New Risk Amount: $"))

    trades[trade_index]["risk"] = new_risk

    print("Trade updated successfully.")