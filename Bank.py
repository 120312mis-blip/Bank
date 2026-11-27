import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "balance.txt")
history_path = os.path.join(base_dir, "data", "history.txt")

class BankAccount:
    def __init__(self, file_path, history_path):
        self.file_path = file_path
        self.history_path = history_path
        self.balance = self.load_balance()

    def deposit(self, amount):
        if amount <= 0:
            return False, ("Сумма пополнения должна быть больше нуля")
        self.balance += amount
        self.add_to_history(f"Пополнение: + {amount}")
        self.save_balance()
        return True, f"Пополнение успешно. Текущий баланс: {self.balance}"
    
    def withdraw(self, amount):
        if amount <= 0:
            return False, "Сумма снятия должна быть больше нуля"
        if self.balance < amount:
            return False, "Недостаточно средств."
        self.balance -= amount
        self.add_to_history(f"Снятие: - {amount}")
        self.save_balance()
        return True, f"Снятие успешно. Текущий баланс: {self.balance}"

    def show_balance(self):
        return f"Текущий баланс: {self.balance}"
    
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
            return "\nИстория операций пока пуста."
    
account = BankAccount(file_path, history_path)
print(account.show_balance())

while True:
    print("1 - Пополнить \n2 - Снять \n3 - Посмотреть баланс \n4 - Выход \n5 - История операций")
    choice = input("Выберите действие: ")
    
    if choice == "1":
        try:
            amount = float(input("Введите сумму для пополнения: "))
            success, message = account.deposit(amount)
            print(message)
        except ValueError:
            print("Ошибка! Введите число.")
            continue

    elif choice == "2":
        try:
            amount = float(input("Введите сумму для снятия: "))
            success, message = account.withdraw(amount)
            print(message)
        except ValueError:
            print("Ошибка! Введите число.")
            continue

    elif choice == "3":
        print(account.show_balance())

    elif choice == "4":
        print("До свидания!")
        break

    elif choice == "5":
        print(account.show_history())

    else:
        print("Неизвестная команда. Пожалуйста, выберите от 1 до 5.")
