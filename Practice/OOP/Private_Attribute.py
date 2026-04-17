class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance


    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount >0:
            self.__balance = self.__balance+amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -=amount
        else:
            print("Invalid withdrawal amount.")

account = BankAccount("Bhavika" , 5000)
print(account.account_holder)

print(account.get_balance())
account.deposit(1000)
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())

print(account._BankAccount__balance)
