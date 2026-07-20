# Trade Journal CLI
A modular command-line trading journal built with Python for recording, managing, and analyzing trading activity.

The application supports persistent local storage, automatic saving, trade editing, performance statistics, pair/market filtering, and session-based analysis.

Features
Add new trades
View all saved trades
Edit existing trades
Delete trades
Automatically save changes
Automatically load saved trades when the program starts
Record:
Pair or market
Trading session
Direction
Risk amount
Risk-to-reward ratio
Result
Notes
Date and time
View overall trading statistics
View statistics for a specific pair or market
View statistics for a specific trading session
Accept abbreviated inputs:
B or BUY
S or SELL
W or WIN
L or LOSS
Validate numeric and menu inputs
Recover safely from a missing or unreadable JSON file
Statistics

The journal currently calculates:

Total trades
Wins
Losses
Win rate
Total risk
Average risk
Highest risk
Pair/market-specific performance
Session-specific performance
Project Structure
trade-journal-cli/
├── main.py
├── trade_system.py
├── stats_system.py
├── storage_system.py
├── README.md
└── .gitignore
main.py

Controls the application menu and coordinates the other systems.

trade_system.py

Handles:

Trade creation
Trade display
Trade editing
Trade deletion
Input validation
Direction and result normalization
Automatic timestamps
stats_system.py

Handles:

Overall statistics
Pair/market filtering
Session filtering
Risk calculations
Win-rate calculations
storage_system.py

Handles:

Saving trades to JSON
Loading saved trades
Missing-file handling
Corrupted JSON protection
Requirements
Python 3

No third-party packages are required.

Running the Project

Clone the repository:

git clone https://github.com/isaacdev-builds/trade-journal-cli.git

Enter the project folder:

cd trade-journal-cli

Run the application:

python main.py

On some Windows systems, use:

py main.py
Example Menu
=== TRADE JOURNAL CLI ===

1. Add Trade
2. View Trades
3. Edit Trade
4. Delete Trade
5. View Overall Stats
6. View Pair/Market Stats
7. View Session Stats
8. Exit
Example Trade
Date: 2026-07-19 07:30 PM
Pair/Market: EURUSD
Session: NY
Direction: BUY
Risk: $50.00
RR: 3.0:1
Result: WIN
Notes: London low sweep followed by bullish displacement.
Data Storage

Trades are stored locally inside:

trades.json

This file is excluded from Git version control through .gitignore.

That means:

Personal trading data stays on the user's computer
Test trades are not uploaded to GitHub
Each user receives a separate local journal
The file is created automatically after the first trade is saved
Concepts Practiced

This project was built to practice:

Python functions
Modules and imports
Lists and dictionaries
Loops and conditional logic
CRUD operations
JSON persistence
Input validation
Error handling
Data normalization
Filtering and derived statistics
Separation of concerns
Modular software architecture
Git and GitHub workflow
Architecture

The program follows a modular structure in which each file has one main responsibility:

User input
    ↓
main.py
    ↓
Trade, statistics, or storage system
    ↓
Updated data and output

This keeps the code easier to understand, test, maintain, and extend.

Future Improvements

Possible future additions include:

Breakeven trade support
Stronger validation for direction, result, and session
Date-range filtering
Monthly and weekly reports
Average RR statistics
Profit and loss tracking
CSV export
Database storage
REST API version
Web-based interface
User accounts and authentication
Project Status

Core command-line version complete.

This project serves as the first portfolio project in a longer backend-development learning path.

Author

Isaac Garcia

Aspiring backend developer building trading tools, data systems, and practical Python applications.
