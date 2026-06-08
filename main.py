from trade_system import create_trade

trades = []

print("=== TRADE JOURNAL CLI ===")

while True:
    print("\n1. Add Trade")
    print("2. View Trades")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        trade = create_trade()
        trades.append(trade)

        print("Trade Added:")
        print(trade)

    elif choice == "2":
        if len(trades) == 0:
            print("\nNo trades added yet.")
        else:
            print("\n=== SAVED TRADES ===")
            for trade in trades:
                print(trade)

    elif choice == "3":
        print("Exiting journal")
        break

    else:
        print("Invalid option")