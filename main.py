from trade_system import create_trade, display_trades
from stats_system import display_stats

trades = []

print("=== TRADE JOURNAL CLI ===")

while True:
    print("\n1. Add Trade")
    print("2. View Trades")
    print("3. View Stats")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == "1":
        trade = create_trade()
        trades.append(trade)

        print("Trade Added:")
        print(trade)

    elif choice == "2": 
        display_trades(trades)
        
    elif choice == "3":
        display_stats(trades)

    elif choice == "4":
        print("Exiting journal")
        break

    else:
        print("Invalid option")