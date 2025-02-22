def showbalance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit(balance):
    try:
        amount = float(input("Enter your deposit amount: "))
        if amount < 0:
            print("That's not a valid amount.")
            return balance
        else:
            balance += amount
            print(f"Successfully deposited ${amount:.2f}")
            return balance
    except ValueError:
        print("Invalid input. Please enter a number.")
        return balance

def withdraw(balance):
    try:
        amount = float(input("Enter your withdrawal amount: "))
        if amount > balance:
            print("Insufficient balance.")
            return balance
        elif amount < 0:
            print("Invalid withdrawal amount.")
            return balance
        else:
            balance -= amount
            print(f"Successfully withdrew ${amount:.2f}")
            return balance
    except ValueError:
        print("Invalid input. Please enter a number.")
        return balance

balance = 0  
while_running = True

while while_running:
    print("\nWelcome to SV Banking...")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            showbalance(balance)
        elif choice == 2:
            balance = deposit(balance)
        elif choice == 3:
            balance = withdraw(balance)
        elif choice == 4:
            print("Thank you for using SV Banking!")
            while_running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
