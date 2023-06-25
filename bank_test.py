import unittest
import bank


class Bank_test(unittest.TestCase):

    def test_Bank_Can_Register_customer(self):
        my_bank = bank.Bank()
        my_bank.register_customers("emmanuel", "segun", "07038243709", 111)
        self.assertEqual(1, my_bank.get_size())

    def test_bank_can_register_more_than_two_account(self):
        my_bank = bank.Bank()
        my_bank.register_customers("emmanuel", "segun", "07038243709", 111)
        my_bank.register_customers("emmanuel", "segun", "07038243709", 111)
        self.assertEqual(2, my_bank.get_size())

    def test_bank_can_generate_account_number_by_depositing_to_account(self):
        my_bank = bank.Bank()
        my_bank.register_customers("emmanuel", "ola", "09037458890", 111)
        my_bank.register_customers("emmanuel", "ola", "09037375208", 121)
        my_bank.deposit("9037375208", 5000)
        balance = my_bank.check_balance("9037375208", 121)
        self.assertEqual(5000, balance)

    def test_bank_can_deposit_twice_to_account_number(self):
        my_bank = bank.Bank()
        my_bank.register_customers("emmanuel", "ola", "09037458890", 111)
        my_bank.register_customers("emmanuel", "ola", "09037375208", 121)
        my_bank.deposit("9037375208", 5000)
        my_bank.deposit("9037375208", 5000)
        balance = my_bank.check_balance("9037375208", 121)
        self.assertEqual(10000, balance)

    def test_bank_can_deposit_to_two_different_account_number(self):
        my_bank = bank.Bank()
        my_bank.register_customers("emmanuel", "ola", "09037458890", 111)
        my_bank.register_customers("emmanuel", "ola", "09037375208", 121)
        my_bank.deposit("9037375208", 5000)
        my_bank.deposit("9037458890", 5000)
        balance = my_bank.check_balance("9037375208", 121)
        balance2 = my_bank.check_balance("9037458890", 111)
        self.assertEqual(5000, balance)
        self.assertEqual(5000, balance2)

    def test_bank_can_withdraw_from_account(self):
        my_bank = bank.Bank()
        my_bank.register_customers("emmanuel", "ola", "09037458890", 111)
        my_bank.register_customers("emmanuel", "ola", "09037375208", 121)
        my_bank.deposit("9037375208", 5000)
        balance = my_bank.check_balance("9037375208", 121)
        self.assertEqual(5000, balance)
        my_bank.withdraw("9037375208", 3000, 121)
        balance = my_bank.check_balance("9037375208", 121)
        self.assertEqual(2000, balance)

    def test_bank_can_withdraw_from_both_account(self):
        my_bank = bank.Bank()
        my_bank.register_customers("emmanuel", "ola", "09037458890", 111)
        my_bank.register_customers("emmanuel", "ola", "09037375208", 121)
        my_bank.deposit("9037375208", 5000)
        my_bank.deposit("9037458890", 5000)
        balance = my_bank.check_balance("9037375208", 121)
        balance2 = my_bank.check_balance("9037458890", 111)
        self.assertEqual(5000, balance)
        self.assertEqual(5000, balance2)
        my_bank.withdraw("9037375208", 3000, 121)
        balance = my_bank.check_balance("9037375208", 121)
        self.assertEqual(2000, balance)
        my_bank.withdraw("9037458890", 3000, 111)
        balance2 = my_bank.check_balance("9037458890", 111)
        self.assertEqual(2000, balance2)

    def test_bank_can_transfer_to_account(self):
        my_bank = bank.Bank()
        my_bank.register_customers("emmanuel", "ola", "09037458890", 111)
        my_bank.register_customers("emmanuel", "ola", "09037375208", 121)
        my_bank.deposit("9037375208", 5000)
        my_bank.transfer("9037375208", 2000, 121, "9037458890")
        balance = my_bank.check_balance("9037375208", 121)
        self.assertEqual(2000, balance)











