class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Updated balance: {self.balance}")

    def describe(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        print(f"Interest Rate: {self.interest_rate}%")



savings = SavingsAccount("Maria", 10000, 3)

savings.deposit(1000)
savings.describe()
print(f"Is SavingsAccount an instance of BankAccount? {isinstance(savings, BankAccount)}")
