
class BankAccount:
    def __init__(self , account_number : str,balance : float = 0.0 ):

        self._account_number = account_number
        self._balance = balance
        self._transactions = []



    def get_transactions (self):
        return self._transactions.copy()
    
    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance
     

    def deposit(self, amount : float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        self._transactions.append(f"Deposited {amount}")


    def withdraw(self, amount : float) -> None:
        if amount <= 0 :
            raise ValueError("withdraw amount must be positive")
        
        if amount > self._balance :
            raise ValueError("You do not have enough funds to complete this transaction.")
        
        

        self._balance -= amount
        self._transactions.append(f"withdraw {amount}")

    def get_statement(self) -> str:
        statement = f"Account: {self._account_number}\n"
        statement += f"Balance: {self._balance}\n"
        statement += "Transactions:\n"

        for t in self._transactions:
            statement += f"- {t}\n"

        return statement
  
