class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("opening balance cannot be negative")

        self._owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("insufficient funds")

        self._balance -= amount

    def __str__(self):
        return f"{self._owner}: {self._balance:.2f}"