import datetime


class BankAccount:
    def __init__(self , account_number : int , initial_balance : float = 0.0 ):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self._account_number = account_number
        self._balance = float(initial_balance)
        self._transactions: list[str] = []

        if initial_balance > 0:
            self._transactions.append(
                f"{datetime.now()} - Initial deposit: {initial_balance:.2f}"
            )


    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    def account_deposit(self):
        pass
    def account_withdraw(self):
        pass










account = BankAccount("ACC123456")  # Create account with initial balance of 0

# Deposit money
account.deposit(1000.0)
print(account.balance)  # Should show 1000.0

# Withdraw money
account.withdraw(300.0)
print(account.balance)  # Should show 700.0

# Attempt invalid withdrawal (should raise an exception)
account.withdraw(800.0)  # Should fail - insufficient funds

# Attempt to modify balance directly (should fail)
account.balance = 5000.0  # Should raise an error - balance is protected

# View account information
print(account.get_statement())  # Display account details