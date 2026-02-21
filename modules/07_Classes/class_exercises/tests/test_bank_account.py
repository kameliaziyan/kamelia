import unittest
from solution.bank_account import BankAccount   


class TestBankAccount(unittest.TestCase):

    def test_bank(self) -> None:
        account = BankAccount("ACC123456")

        account.deposit(1500)
        assert account.balance == 1500

        account.withdraw(400)
        assert account.balance == 1100


    def test_wrong_balance(self) -> None:
        account = BankAccount("ACC123456")

        with self.assertRaises(AttributeError):
            setattr(account, "balance", 5000.0)



    def test_invalid_operations(self) -> None:
        account = BankAccount("ACC123456")

    
        with self.assertRaises(ValueError):
            account.deposit(-100)





