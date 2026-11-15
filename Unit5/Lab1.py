
# To develop a bank account system using classes and objects to perform basic banking operations.

class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print("\nAccount Details")
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Creating an account
name = input("Enter Account Holder Name: ")
acc_no = input("Enter Account Number: ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(name, acc_no, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Account")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice!")
