import unittest
from solution.bank_account import BankAccount   


class TestBankAccount(unittest.TestCase):

    def test_bank(self) -> None:
        account = BankAccount("ACC123456")

        account.deposit(1000)
        assert account.balance == 1000

        account.withdraw(300)
        assert account.balance == 700


    def test_wrong_balance(self) -> None:
        account = BankAccount("ACC123456")

        with self.assertRaises(AttributeError):
            setattr(account, "balance", 5000.0)



    def test_invalid_operations(self) -> None:
        account = BankAccount("ACC123456")

    
        with self.assertRaises(ValueError):
            account.deposit(-100)





