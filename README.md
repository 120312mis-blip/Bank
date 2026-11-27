# 🏦 Console Bank Account Simulator (Bank CLI)

An educational Python pet project demonstrating Object-Oriented Programming (OOP), file system operations, and exception handling.

The application simulates basic bank account operations and automatically saves progress between sessions.

## ✨ Features
* **Deposit funds** with input validation to ensure positive amounts.
* **Withdraw funds** with balance sufficiency checks.
* **Check current balance** (default starting balance is `1000.0`).
* **Transaction history:** automatic logging of all deposits and withdrawals into a separate file.
* **Auto-save:** data is stored locally in the `data/` directory and persists after restarting the program.

## 🛠 Tech Stack
* **Python 3** (uses only the built-in `os` module; no external dependencies required).

## 🚀 How to Run

1. Clone the repository to your local machine:
```bash
git clone https://github.com
```

2. Navigate to the project directory:
```bash
cd Bank
```

3. Run the main script (replace `main.py` with your actual script filename if different):
```bash
python main.py
```

## 📂 Project Structure
```text
Bank/
├── data/               # Created automatically on the first run
│   ├── balance.txt     # Current user balance
│   └── history.txt     # Log of all transactions
├── main.py             # Main application source code
└── README.md           # Project documentation
```

## 🤝 Feedback & Contributions
This project was built while learning Python and OOP. Any constructive feedback, code review tips, or feature ideas are welcome in the **Issues** section!
