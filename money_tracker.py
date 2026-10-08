print("===== MY MONEY TRACKER =====")

balance = float(input("How much money do you have? £"))

print("\n1. Add income")
print("2. Add expense")

choice = input("Choose 1 or 2: ")

amount = float(input("Enter amount: £"))

if choice == "1":
    balance = balance + amount
    print("Income added!")

elif choice == "2":
    balance = balance - amount
    print("Expense added!")

else:
    print("Invalid choice!")

print("Your balance is £", round(balance, 2))