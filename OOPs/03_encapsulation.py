# Encapsulation keeps data and the methods that use it together.
# The underscore is a Python hint that balance is meant for internal use.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def show_balance(self):
        print(f"Balance: ₹{self._balance}")


account = BankAccount(1000)
account.deposit(500)
account.show_balance()
