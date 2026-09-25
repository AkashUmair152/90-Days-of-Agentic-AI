# 🔥 Project 1 — Bank Account System

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return self.balance
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return self.balance
        if amount > self.balance:
            print("Insufficient funds.")
            return self.balance
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

# Execution & Testing
if __name__ == "__main__":
    account = BankAccount("Akash", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(account.get_balance())  # Output: 1300.0