
'''ATM Management
==================
class variable/static variable:bank name
instance variable:account_no,account holder,balance=1000
balance_enquiry() -> current balance
deposit() ->amount:4000,
withdraw() ->amoun:10000 ,insufficient balance
'''   

class ATM:
    bank_name = "ABC Bank"

    def __init__(self, account_no, account_holder):
        self.account_no = account_no
        self.account_holder = account_holder
        self.balance = 1000
        
    def display(self):
        print(f"Account no : {self.account_no}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Balance : {self.balance}")
        
    
    def balance_enquiry(self):
        print(f"Current Balance = {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited Amount = {amount}")
        print(f"Current Balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrawn Amount = {amount}")
            print(f"Current Balance = {self.balance}")
        else:
            print("Insufficient Balance")


account = ATM("1234xxxxxxx", "Jahana")

account.display()
print("=======================")
account.balance_enquiry()
print("=======================")
account.deposit(4000)
print("=======================")
account.withdraw(10000)
