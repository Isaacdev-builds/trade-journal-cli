from trade_system import create_trade, display_trades, delete_trade, edit_trade
from stats_system import display_stats
from storage_system import save_trades, load_trades

trades = load_trades()

print("=== TRADE JOURNAL CLI ===")

while True:
    print("\n1. Add Trade")
    print("2. View Trades")
    print("3. View Stats")
    print("4. Save Trades")
    print("5. Exit")
    print("6. Delete Trade")
    print("7. Edit Trade")
    
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
        save_trades(trades)

    elif choice == "5":
        print("Exiting journal")
        break

    elif choice == "6":
        display_trades(trades)
        trade_number = int(input("Enter trade number to delete: "))
        delete_trade(trades, trade_number)

    elif choice == "7":
        display_trades(trades)
        trade_number = int(input("Enter trade number to edit: "))
        edit_trade(trades, trade_number)

    else:
        print("Invalid option")