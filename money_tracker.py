#This is a simple money tracker program that allows users to add income and expenses, check their balance, and view their transaction history.


print("===== MY MONEY TRACKER =====")

balance = float(input("How much money do you have? £"))

transactions = []
while True:
    print("\n1. Add income")
    print("2. Add expense")
    print("3. Check balance")
    print("4. Exit")
    choice = input("Choose 1, 2, 3 or 4: ")

    if choice == "4":
        print("Exiting...")
        break

    amount = float(input("Enter amount: £"))


    if choice == "1":
        balance = balance + amount
        transactions.append(f"Income: +£{amount:.2f}")
        print("Income added!")

    elif choice == "2":
        balance = balance - amount
        transactions.append(f"Expense: -£{amount:.2f}")
        print("Expense added!")
    elif choice == "3":
            print(f"Your balance is £{balance:.2f}")
            continue
    
    else:
        print("Invalid choice!")

print("\n===== TRANSACTION HISTORY =====")

if len(transactions) == 0:
    print("No transactions yet.")

else:
    for transaction in transactions:
        print(transaction)

print(f"\nYour balance is £{balance:.2f}")