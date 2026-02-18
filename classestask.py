class BankAccount:
    def __init__(self, account_number, owner_name, balance=0.0, date_opened="2026-02-18"):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.date_opened = date_opened

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_info(self):
        print(" Account Information ")
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")
        



account1 = BankAccount("001", "Alice", 500.0, "2026-01-10")
account2 = BankAccount("002", "Bob", 1000.0, "2026-01-15")


account1.deposit(200)
account1.withdraw(100)
account1.display_info()

account2.deposit(500)
account2.withdraw(1200) 
account2.display_info()
