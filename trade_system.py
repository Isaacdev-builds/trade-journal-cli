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