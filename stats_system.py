def display_stats(trades):
    total_trades = len(trades)

    if total_trades == 0:
        print("\nNo trades available for stats.")
        return

    wins = 0
    losses = 0

    total_risk = 0
    highest_risk = 0

    for trade in trades:
        total_risk += trade["risk"]
        
        if trade["risk"] > highest_risk:
            highest_risk = trade["risk"]

        if trade["result"] == "WIN":
            wins += 1
        elif trade["result"] == "LOSS":
            losses += 1

    win_rate = (wins / total_trades) * 100
    average_risk = total_risk / total_trades

    print("\n=== TRADE STATS ===")
    print(f"Total Trades: {total_trades}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Total Risk: ${total_risk:.2f}")
    print(f"Average Risk: ${average_risk:.2f}")
    print(f"Highest Risk: ${highest_risk:.2f}")

def display_pair_stats(trades):
    pair = input("Enter pair to analyze: ").upper()

    filtered_trades = []

    for trade in trades:
        if trade["pair"] == pair:
            filtered_trades.append(trade)

    if len(filtered_trades) == 0:
        print("No trades found for that pair.")
        return

    print(f"\n=== PAIR/MARKET STATS: {pair} ===")
    display_stats(filtered_trades)