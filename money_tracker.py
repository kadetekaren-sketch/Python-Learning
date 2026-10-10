print("===== MY MONEY TRACKER =====")

balance = float(input("How much money do you have? £"))

transactions = []

print("\n1. Add income")
print("2. Add expense")

choice = input("Choose 1 or 2: ")

amount = float(input("Enter amount: £"))

if choice == "1":
    balance = balance + amount
    transactions.append(f"Income: +£{amount:.2f}")
    print("Income added!")

elif choice == "2":
    balance = balance - amount
    transactions.append(f"Expense: -£{amount:.2f}")
    print("Expense added!")

else:
    print("Invalid choice!")

print("\n===== TRANSACTION HISTORY =====")

if len(transactions) == 0:
    print("No transactions yet.")

else:
    for transaction in transactions:
        print(transaction)

print(f"\nYour balance is £{balance:.2f}")