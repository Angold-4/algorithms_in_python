# Angold4 20200513
from CreditCard import CreditCard
from Range import Range


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    __slots__ = '_apr'

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)  # Return True if charge was processed
        if not success:  # Return False and assess $5 fee if charge is denied
            self._balance += 5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance"""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


if __name__ == "__main__":
    """Test"""
    wallet = []
    wallet.append(PredatoryCreditCard('John Bowman', 'California Savings',
                                      '5391 0375 9387 5309', 2500, 0.0825))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Federal',
                                      '3485 0399 3395 1954', 3500, 0.0800))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Finance',
                                      '5391 0375 9387 5309', 5000, 0.0750))
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in Range(3):
        wallet[c].process_month()
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()

"""
Customer = John Bowman
Bank = California Savings
Account = 5391 0375 9387 5309
Limit = 2500
Balance = 136.90140348539404
New balance = 36.90140348539404

Customer = John Bowman
Bank = California Federal
Account = 3485 0399 3395 1954
Limit = 3500
Balance = 273.75005618992094
New balance = 173.75005618992094
New balance = 73.75005618992094

Customer = John Bowman
Bank = California Finance
Account = 5391 0375 9387 5309
Limit = 5000
Balance = 410.466326961911
New balance = 310.466326961911
New balance = 210.46632696191102
New balance = 110.46632696191102
New balance = 10.466326961911022
"""
