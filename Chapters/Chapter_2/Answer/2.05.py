# Angold4 20200515 2.05.py
import sys; sys.path.append('..')  # Change the relative path
from CreditCard import CreditCard


class FCreditCard(CreditCard):
    def charge(self, price):
        try:
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        except TypeError as e:
            print("Price need to be number!", e)

    def make_payment(self, amount):
        try:
            if amount < 0:
                raise ValueError("amount must be positive!")
            self._balance -= amount
        except TypeError as e:
            print("Amount need to be number!", e)


"""Test"""

if __name__ == "__main__":
    F = FCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500)
    F.charge('3')  # Price need to be number! can only concatenate str (not "int") to str
