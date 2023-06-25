from bank_account.account import Account


class Bank:

    def __init__(self):
        self.__account = []

    def register_customers(self, firstname, lastname, phone_number, pin):
        account_number1 = self.__generate_account_number(phone_number)
        account1 = Account(firstname, lastname, phone_number, pin)
        self.__account.append(account1)
        account1.account_number = account_number1

    def __generate_account_number(self, phone_number):
        account_number = phone_number[1:]
        return account_number

    def get_size(self):
        return len(self.__account)

    def search_account_number(self, searched_account_number):
        for account1 in self.__account:
            if account1.account_number == searched_account_number:
                return account1
            else:
                raise TypeError("account number not found un the list")

    def deposit(self, account_number, amount):
        account = self.search_account_number(account_number)
        account.deposit_Money(amount)

    def check_balance(self, account_number, pin):
        account = self.search_account_number(account_number)
        balance = account.check_balance(pin)
        return balance

    def withdraw(self, account_number, amount, pin):
        account = self.search_account_number(account_number)
        account.withdrawn_Money(amount, pin)

    def transfer(self, sender_account_number, amount, pin, receiver_account_number):
        account = self.search_account_number(sender_account_number)
        value =self.verify(receiver_account_number)
        value
    def verify(self, receiver_account_number):
        account = self.search_account_number(receiver_account_number)
        myAccount = account
        return myAccount





