from datetime import datetime

print("==============================")
print("     DIGITAL TIME CAPSULE")
print("==============================")

print("\nA little message for your future self.")

name = input("\nWhat is your name? ")
message = input("Write a message to your future self: ")

print("\nWhen do you want to open your time capsule?")
unlock_date = input("Enter a date (YYYY-MM-DD): ")

print("\n===== YOUR TIME CAPSULE =====")
print("Created by:", name)
print("Your message:", message)
print("Unlock date:", unlock_date)
print("============================")