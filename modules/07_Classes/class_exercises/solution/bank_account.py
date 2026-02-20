class BankAccount:
    def __init__(self, account_number: str, balance: float = 0):
        self._account_number = account_number
        self._balance = balance
        self._transactions: list[str] = []

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def transactions(self) -> list[str]:
        return self._transactions.copy()

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        self._transactions.append(f"Deposited {amount}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self._balance:
            raise ValueError(
                "You do not have enough funds to complete this transaction."
            )

        self._balance -= amount
        self._transactions.append(f"Withdrew {amount}")

    def get_statement(self) -> str:
        lines = [
            f"Account: {self._account_number}",
            f"Balance: {self._balance}",
            "Transactions:",
            *[f"- {tx}" for tx in self._transactions],
        ]
        return "\n".join(lines)
