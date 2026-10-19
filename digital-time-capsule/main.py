from datetime import datetime
import json
import os

print("==============================")
print("      DIGITAL TIME CAPSULE")
print("==============================")

print("\nA little message for your future self.")

name = input("\nWhat is your name? ")
message = input("Write a message to your future self: ")

print("\nWhen do you want to open your time capsule?")
unlock_date = input("Enter a date (YYYY-MM-DD): ")

# Check whether the date is valid
try:
    unlock_date = datetime.strptime(unlock_date, "%Y-%m-%d").date()

    if unlock_date <= datetime.today().date():
        print("Choose a future date!")
    else:
        capsule = {
            "name": name,
            "message": message,
            "unlock_date": str(unlock_date)
        }

        # Save the capsule to a file
        with open("capsule.json", "w") as file:
            json.dump(capsule, file, indent=4)

        print("\nYour time capsule has been saved!")
        print("Unlock date:", unlock_date)

except ValueError:
    print("Invalid date! Use YYYY-MM-DD.")