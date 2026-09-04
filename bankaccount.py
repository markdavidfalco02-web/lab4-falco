class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Updated balance: {self.balance}")

    def describe(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")



class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        # Reuse parent class constructor
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        # Extend parent's deposit() method instead of replacing it
        super().deposit(amount)
        print(f"Account interest rate: {self.interest_rate}%")



savings = SavingsAccount("Maria", 10000, 3)


print("--- Calling deposit() ---")
savings.deposit(500)  # Deposit an example amount


print("\n--- Calling describe() ---")
savings.describe()


print("\n--- Instance Check ---")
is_bank_account = isinstance(savings, BankAccount)
print(f"Is this SavingsAccount also a BankAccount? {is_bank_account}")


