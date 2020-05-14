# Angold4 20200515 2.04.py (2.01 - 2.03 were not programs)
class Flower:
    def __init__(self, name, petal, price):
        if type(name) is str and type(petal) is int and type(price) is float:
            self._name = name
            self._petal = petal
            self._price = price
        else:
            raise ValueError("Type:{name: str, petal: int, price: float}")

    def set_name(self, newname):
        if type(newname) is str:
            self._name = newname
        else:
            print("Error! Must be Str!")

    def set_petal(self, newpetal):
        if type(newpetal) is int:
            self._petal = newpetal
        else:
            print("Error! Must be Int!")

    def set_price(self, newprice):
        if type(newprice) is float:
            self._price = newprice
        else:
            print("Error! Must be Float!")

    def get_name(self):
        return self._name

    def get_petal(self):
        return self._petal

    def get_price(self):
        self._price = str(self._price)
        self._price = '$' + self._price
        return self._price


"""Test"""

if __name__ == "__main__":
    A = Flower('Jasmine', 6, 8.00)
    print(A.get_name())   # Jasmine
    print(A.get_petal())  # 6
    print(A.get_price())  # $8.0
