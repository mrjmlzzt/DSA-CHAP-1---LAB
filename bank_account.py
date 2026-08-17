class BankAccount:
    """An account that will not let itself go negative."""

    def __init__(self, owner, balance=0):
        # Step 1
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self._owner = owner
        self._balance = balance

    def get_balance(self):
        # Step 2 
        # Return the stored balance. Callers use this instead of reaching
        # into self._balance themselves.
        return self._balance

    def deposit(self, amount):
        # Step 3
        # - raise ValueError if amount is zero or negative
        # - otherwise add it to the balance
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        # Step 4
        # - raise ValueError if amount is zero or negative
        # - raise ValueError if amount is larger than the balance
        # - otherwise subtract it from the balance
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Withdrawal amount cannot exceed the balance")
        self._balance -= amount

    def __str__(self):
        # Step 5
        # Return the owner, a colon, and the balance to two decimal places,
        # for example: Juan: 1500.00
        return f"{self._owner}: {self._balance:.2f}"


if __name__ == "__main__":
    print("BankAccount starter. Run: python test_bank_account.py")
