class BankAccount:
    def __init__(self , account_number : int , balance : int ):
        self.account_number = account_number
        self.balance = balance






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