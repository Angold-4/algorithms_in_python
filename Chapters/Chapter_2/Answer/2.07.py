# Angold4 20200517 2.07.py
import sys; sys.path.append('..')  # Change the relative path
from CreditCard import CreditCard


class BCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit,  balance=0):
        super().__init__(customer, bank, account, limit)
        self._balance = balance


if __name__ == "__main__":
    B = BCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, 100)
    print(B.get_balance())
