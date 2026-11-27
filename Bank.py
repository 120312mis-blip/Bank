import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "balance.txt")
history_path = os.path.join(base_dir, "data", "history.txt")

class BankAccount:
    def __init__(self, balance = 1000):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Сумма пополнения должна быть больше нуля")
            return
        self.balance += amount
        add_to_history(f"Пополнение: + {amount}")
        self.show_balance()
        save_balance(self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть больше нуля")
            return
        if self.balance < amount:
            print("Недостаточно средств.")
            return
        self.balance -= amount
        add_to_history(f"Снятие: - {amount}")
        self.show_balance()
        save_balance(self.balance)

    def show_balance(self):
            print(f"Текущий баланс: {self.balance}")


def load_balance():
    try:
        with open(file_path, "r") as f:
            return float(f.read())
    except FileNotFoundError:
        return 1000.0

def save_balance(balance):
        with open(file_path, "w") as f:
            f.write(str(balance))

def add_to_history(operation_text):
    with open(history_path, "a", encoding="utf-8") as f:
        f.write(operation_text + "\n")

def show_history():
    try:
        with open(history_path, "r", encoding="utf-8") as f:
            print("\n--- История операций ---")
            print(f.read())
    except FileNotFoundError:
        print("\nИстория операций пока пуста.")

account = BankAccount(load_balance())
account.show_balance()

while True:
    print("1 - Пополнить \n2 - Снять \n3 - Посмотреть баланс \n4 - Выход \n5 - История операций")
    choice = input("Выберите действие: ")
    
    if choice == "1":
        try:
            amount = float(input("Введите сумму для пополнения: "))
            account.deposit(amount)
        except ValueError:
            print("Ошибка! Введите число.")
            continue

    elif choice == "2":
        try:
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        except ValueError:
            print("Ошибка! Введите число.")
            continue

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("До свидания!")
        break

    elif choice == "5":
        show_history()

    else:
        print("Неизвестная команда. Пожалуйста, выберите от 1 до 5.")
