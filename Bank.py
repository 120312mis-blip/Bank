import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "balance.txt")
history_path = os.path.join(base_dir, "data", "history.txt")

class BankAccount:
    def __init__(self, file_path, history_path):
        self.file_path = file_path
        self.history_path = history_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.balance = self.load_balance()

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than zero."
        self.balance += amount
        self.add_to_history(f"Deposit: + {amount}")
        self.save_balance()
        return True, f"Deposit successful. Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."
        if self.balance < amount:
            return False, "Insufficient funds."
        self.balance -= amount
        self.add_to_history(f"Withdrawal: - {amount}")
        self.save_balance()
        return True, f"Withdrawal successful. Current balance: {self.balance}"

    def show_balance(self):
        return f"Current balance: {self.balance}"

    def load_balance(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return float(f.read())
        except FileNotFoundError:
            return 1000.0

    def save_balance(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(str(self.balance))

    def add_to_history(self, operation_text):
        with open(self.history_path, "a", encoding="utf-8") as f:
            f.write(operation_text + "\n")

    def show_history(self):
        try:
            with open(self.history_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "\nTransaction history is empty."

account = BankAccount(file_path, history_path)
print(account.show_balance())

while True:
    print("1 - Deposit \n2 - Withdraw \n3 - Check balance \n4 - Exit \n5 - Transaction history")
    choice = input("Choose an action: ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            success, message = account.deposit(amount)
            print(message)
        except ValueError:
            print("Error! Please enter a number.")
            continue

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            success, message = account.withdraw(amount)
            print(message)
        except ValueError:
            print("Error! Please enter a number.")
            continue

    elif choice == "3":
        print(account.show_balance())

    elif choice == "4":
        print("Goodbye!")
        break

    elif choice == "5":
        print(account.show_history())

    else:
        print("Unknown command. Please choose from 1 to 5.")
