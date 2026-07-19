from datetime import datetime

def normalize_direction(value):
    value = value.upper()

    if value == "B":
        return "BUY"

    if value == "S":
        return "SELL"

    return value


def normalize_result(value):
    value = value.upper()

    if value == "W":
        return "WIN"

    if value == "L":
        return "LOSS"

    return value

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def create_trade():

    pair = input("Pair/Market: ").upper()
    session = input("Session (e.g., NY, LDN, ASIA): ").upper()
    direction = normalize_direction(input("Direction (BUY/SELL or B/S): "))
    risk = get_numeric_input("Risk Amount: $")
    rr = get_numeric_input("RR: ")
    result = normalize_result(input("Result (WIN/LOSS or W/L): "))
    notes = input("Notes (optional): ")

    created_at = datetime.now().strftime("%Y-%m-%d %I:%M %p")

    trade = {
        "created_at": created_at,
        "pair": pair,
        "session": session,
        "direction": direction,
        "risk": risk,
        "rr": rr,
        "result": result,
        "notes": notes
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
        print(f"Session: {trade.get('session', 'No session recorded')}")
        print(f"Direction: {trade['direction']}")
        print(f"Risk: ${trade['risk']:.2f}")
        print(f"RR: {trade['rr']}:1")
        print(f"Result: {trade['result']}")
        print(f"Notes: {trade.get('notes') or 'No notes recorded'}")
        print("-" * 20)

def delete_trade(trades, trade_number):
    trade_index = trade_number - 1

    if trade_index < 0 or trade_index >= len(trades):
        print("Invalid trade number.")
        return False

    deleted_trade = trades.pop(trade_index)

    print("\nTrade deleted:")
    print(f"Pair/Market: {deleted_trade['pair']}")
    print(f"Session: {deleted_trade.get('session', 'No session recorded')}")
    print(f"Direction: {deleted_trade['direction']}")
    print(f"Risk: ${deleted_trade['risk']:.2f}")
    print(f"RR: {deleted_trade['rr']}:1")
    print(f"Result: {deleted_trade['result']}")
    print(f"Notes: {deleted_trade.get('notes') or 'No notes recorded'}")

    return True

def edit_trade(trades, trade_number):
    trade_index = trade_number - 1

    if trade_index < 0 or trade_index >= len(trades):
        print("Invalid trade number.")
        return False

    trade = trades[trade_index]

    print("\nEditing Trade")
    print("1. Pair/Market")
    print("2. Direction")
    print("3. Risk")
    print("4. RR")
    print("5. Result")
    print("6. Session")
    print("7. Notes")

    field_choice = input("Select field to edit: ")

    if field_choice == "1":
        trade["pair"] = input("New Pair/Market: ").upper()

    elif field_choice == "2":
        trade["direction"] = normalize_direction(
            input("New Direction (BUY/SELL or B/S): ")
        )

    elif field_choice == "3":
        trade["risk"] = get_numeric_input("New Risk Amount: $")

    elif field_choice == "4":
        trade["rr"] = get_numeric_input("New RR: ")

    elif field_choice == "5":
        trade["result"] = normalize_result(
            input("New Result (WIN/LOSS or W/L): ")
        )

    elif field_choice == "6":
        trade["session"] = input("New Session: ").upper()

    elif field_choice == "7":
        trade["notes"] = input("New Notes: ")

    else:
        print("Invalid field choice.")
        return False

    print("Trade updated successfully.")
    return True