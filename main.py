from trade_system import create_trade, display_trades, delete_trade, edit_trade, get_integer_input
from stats_system import display_stats, display_pair_stats, display_session_stats
from storage_system import save_trades, load_trades

def main():
    trades = load_trades()

    print("=== TRADE JOURNAL CLI ===")

    while True:
        print("\n1. Add Trade")
        print("2. View Trades")
        print("3. Edit Trade")
        print("4. Delete Trade")
        print("5. View Overall Stats")
        print("6. View Pair/Market Stats")
        print("7. View Session Stats")
        print("8. Exit")
        choice = input("Select option: ")

        if choice == "1":
            trade = create_trade()
            trades.append(trade)
            save_trades(trades)

            print("\nTrade added successfully!")

        elif choice == "2": 
            display_trades(trades)

        elif choice == "3":
            display_trades(trades)
            trade_number = get_integer_input("Enter trade number to edit: ")
            if edit_trade(trades, trade_number):
                save_trades(trades)

        elif choice == "4":
            display_trades(trades)
            trade_number = get_integer_input("Enter trade number to delete: ")
            if delete_trade(trades, trade_number):
                save_trades(trades)
            
        elif choice == "5":
            display_stats(trades)

        elif choice == "6":
            display_pair_stats(trades)

        elif choice == "7":
            display_session_stats(trades)

        elif choice == "8":
            print("Exiting journal")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

