from datetime import datetime

date_today = datetime.today()
print(date_today)

class BankAccount:
    def __init__(self,acc_no,balance,owner_name,date_opened=date_today):
        self.account_number = acc_no
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid Amount")
        

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds to compete withdrawal")
        else:
            self.balance -= amount
        

    def display_info(self):
        print("--------ACC. DETAILS---------")
        print(f"Owner Name: {self.owner_name}")
        print(f"Acc. No: {self.account_number}")
        print(f"Current Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")
        print("-------End of Acc Details-------\n")


#Account 1 object
b_account1 = BankAccount("B1",0,"John Doe")
b_account1.deposit(10000)
b_account1.withdraw(3500)
b_account1.display_info()


#Account 2 oobject
b_account2 = BankAccount("B2",0,"Jane Doe",)
b_account2.deposit(15000)
b_account2.withdraw(3500)
b_account2.display_info()
