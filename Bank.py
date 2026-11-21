import os
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "balance.txt")
history_path = os.path.join(base_dir, "data", "history.txt")

def deposit(balance, amount):
    if amount <= 0:
        print("Сумма пополнения должна быть больше нуля")
        return balance
    add_to_history(f"Пополнение: + {amount}")
    return balance + amount

def withdraw(balance, amount):
    if amount <= 0:
        print("Сумма снятия должна быть больше нуля")
        return balance
    if balance < amount:
        print("Недостаточно средств.")
        return balance
    add_to_history(f"Снятие: - {amount}")
    return balance - amount

def show_balance(balance):
    print("На вашем счёту:", balance)

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

balance = load_balance()
show_balance(balance)

while True:
    print("1 - Пополнить \n2 - Снять \n3 - Посмотреть баланс \n4 - Выход \n5 - История операций")
    choice = input("Выберите действие: ")
    
    if choice == "1":
        try:
            amount = float(input("Введите сумму для пополнения: "))
            balance = deposit(balance, amount)
            show_balance(balance)
            save_balance(balance)
        except ValueError:
            print("Ошибка! Введите число.")
            continue

    elif choice == "2":
        try:
            amount = float(input("Введите сумму для снятия: "))
            balance = withdraw(balance, amount)
            show_balance(balance)
            save_balance(balance)
        except ValueError:
            print("Ошибка! Введите число.")
            continue

    elif choice == "3":
        show_balance(balance)

    elif choice == "4":
        print("До свидания!")
        break

    elif choice == "5":
        show_history()

    else:
        print("Неизвестная команда. Пожалуйста, выберите от 1 до 5.")
