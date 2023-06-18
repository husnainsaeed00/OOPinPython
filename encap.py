class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

# Creating an object of the BankAccount class
acount_num= int(input("please enter your account:"))
balance=int(input("input your balance:"))
account = BankAccount(acount_num, balance)
account.deposit(500)   # Depositing 500
account.withdraw(200)  # Withdrawing 200
print(account.balance)  # Output: 1300
