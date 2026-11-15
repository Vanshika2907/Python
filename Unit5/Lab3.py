
# To create a dice simulator using Python's random module to generate random numbers between 1 and 6.
import random

while True:
    print("\nDice Simulator")
    print("1. Roll Dice")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        dice = random.randint(1, 6)
        print("You rolled:", dice)

    elif choice == "2":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice!")
