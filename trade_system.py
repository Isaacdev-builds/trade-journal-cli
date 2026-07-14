from datetime import datetime

def create_trade():

    pair = input("Pair/Market: ").upper()
    direction = input("Direction (BUY/SELL): ").upper()
    while True:
        try:
            risk = float(input("Risk Amount: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for risk.")
    while True:
        try:
            rr = float(input("RR: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for RR.")
    result = input("Result (WIN/LOSS): ").upper()

    created_at = datetime.now().strftime("%Y-%m-%d %I:%M %p")

    trade = {
        "created_at": created_at,
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
        print(f"Date: {trade.get('created_at', 'No date recorded')}")
        print(f"Pair/Market: {trade['pair']}")
        print(f"Direction: {trade['direction']}")
        print(f"Risk: ${trade['risk']:.2f}")
        print(f"RR: {trade['rr']}:1")
        print(f"Result: {trade['result']}")
        print("-" * 20)

def delete_trade(trades, trade_number):
    trade_index = trade_number - 1

    if trade_index < 0 or trade_index >= len(trades):
        print("Invalid trade number.")
        return

    deleted_trade = trades.pop(trade_index)

    print("Trade deleted:")
    print(f"Pair/Market: {deleted_trade['pair']}")
    print(f"Direction: {deleted_trade['direction']}")
    print(f"Risk: ${deleted_trade['risk']:.2f}")
    print(f"RR: {deleted_trade['rr']}:1")
    print(f"Result: {deleted_trade['result']}")

def edit_trade(trades, trade_number):
    trade_index = trade_number - 1

    if trade_index < 0 or trade_index >= len(trades):
        print("Invalid trade number.")
        return

    trade = trades[trade_index]

    print("\nEditing Trade")
    print("1. Pair/Market")
    print("2. Direction")
    print("3. Risk")
    print("4. RR")
    print("5. Result")

    field_choice = input("Select field to edit: ")

    if field_choice == "1":
        trade["pair/market"] = input("New Pair/Market: ").upper()

    elif field_choice == "2":
        trade["direction"] = input("New Direction (BUY/SELL): ").upper()

    elif field_choice == "3":
        while True:
            try:
                trade["risk"] = float(input("New Risk Amount: $"))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for risk.")

    elif field_choice == "4":
        while True:
            try:
                trade["rr"] = float(input("New RR: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for RR.")        

    elif field_choice == "5":
        trade["result"] = input("New Result (WIN/LOSS): ").upper()

    else:
        print("Invalid field choice.")
        return

    print("Trade updated successfully.")