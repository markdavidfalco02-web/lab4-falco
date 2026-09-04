class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.name, "deposited", amount)
        print("Updated Balance:", self.balance)

    def describe(self):
        print(self.name, "- Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        print(self.name, "has an interest rate of", self.interest_rate, "%.")

account = SavingsAccount("Maria", 10000, 3)
account.deposit(2000)
account.describe()
print(isinstance(account, BankAccount))
