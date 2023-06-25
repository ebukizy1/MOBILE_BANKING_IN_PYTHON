import unittest
import account


class Account_Test(unittest.TestCase):

    def test_account_can_deposit(self):
        my_account = Account.account( 111, "emmanuel", "chuk")
        my_account.deposit_Money(5000)
        value = my_account.check_balance(111)
        self.assertEqual(5000, value)

    def test_account_can_withdrawn(self):
        my_account = Account.account( 111, "emmanuel", "chuk")
        my_account.deposit_Money(5000)
        my_account.withdrawn_Money(3000, 111)
        value = my_account.check_balance(111)
        self.assertEqual(2000, value)

    def test_account_can_deposit_negative_amount(self):
        my_account = Account.account( 111, "emmanuel", "chuk")
        my_account.deposit_Money(-1000)
        value = my_account.check_balance(111)
        self.assertEqual(0, value)

    def test_account_can_deposit_twice(self):
        my_account = Account.account( 111, "emmanuel", "chuk")
        my_account.deposit_Money(1000)
        my_account.deposit_Money(1000)
        value = my_account.check_balance(111)
        self.assertEqual(2000, value)

    def test_account_cannot_withdraw_Above_balance(self):
        my_account = Account.account( 111, "emmanuel", "chuk")
        my_account.deposit_Money(10000)
        self.assertRaises(TypeError, my_account.withdrawn_Money, 13000, 111)

    def test_account_cannot_withdraw_above_balance(self):
        my_account = Account.account( 111, "emmanuel", "chuk")
        my_account.deposit_Money(5000)
        self.assertRaises(TypeError, my_account.withdrawn_Money, 7000, 111)

    def test_account_cannot_withdraw_with_wrong_pin(self):
        my_account = Account.account( 111, "emmanuel", "chuk")
        my_account.deposit_Money(5000)
        self.assertRaises(TypeError, my_account.withdrawn_Money, 3000, 211)

    def test_account_withdraw_cannot_check_balance_with_wrong_pin(self):
        my_account = Account.account( 111, "emmanuel", "chuk")
        my_account.deposit_Money(5000)
        self.assertRaises(TypeError, my_account.check_balance, 121)
