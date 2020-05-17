# Angold4 20200518 2.36.py and 2.37.py
from random import randint
RANGE = 100
Ecosysterm = [None]*RANGE
from matplotlib import pyplot as plt


class Animal:

    def __init__(self):
        G = randint(0, 1)
        S = randint(0, 9)
        D = randint(0, RANGE-1)
        _genderdict = {0: False, 1: True}
        self._gender = _genderdict[G]
        self._strength = S
        self._addr = D

    def _set_gender(self, TF):
        if TF is True or TF is False:
            self._gender = TF
        else:
            print("Unsupported Gender(True or False)")

    def get_gender(self):
        return self._gender

    def get_strength(self):
        return int(self._strength)

    def M_S(self):
        """Move or Stay"""
        MoS = randint(0, 1)
        if MoS == 0:
            """Stay"""
            pass
        else:
            Ecosysterm[self._addr] = None
            if self._addr == RANGE-1:
                self._addr -= 1
            elif self._addr == 0:
                self._addr += 1
            else:
                A = randint(0, 1)
                if A == 0:
                    """Previous"""
                    self._addr -= 1
                else:
                    """Next"""
                    self._addr += 1
            """Move"""
            self.goto()


class Bear(Animal):

    def goto(self):
        """Move to Other Addr in Eco"""
        if Ecosysterm[self._addr] is None or isinstance(Ecosysterm[self._addr], Fish):
            Ecosysterm[self._addr] = self
        else:
            if Ecosysterm[self._addr].get_gender() == self.get_gender():
                if Ecosysterm[self._addr].get_strength() < self.get_strength():
                    Ecosysterm[self._addr] = self
            else:
                """Opposite Sex Created a New Child"""
                Bear().goto()


class Fish(Animal):

    def goto(self):
        """Move to Other Addr in Eco"""
        if Ecosysterm[self._addr] is None:
            Ecosysterm[self._addr] = self
        elif isinstance(Ecosysterm[self._addr], Bear):
            """Be Eaten"""
            pass
        else:
            if Ecosysterm[self._addr].get_gender() == self.get_gender():
                if Ecosysterm[self._addr].get_strength() < self.get_strength():
                    Ecosysterm[self._addr] = self

            else:
                """Opposite Sex Created a New Child"""
                Fish().goto()


"""Test"""
if __name__ == "__main__":
    """initialization"""
    X = []
    YF = []
    YB = []
    F = 0
    B = 0
    TERMS = 1000
    # F1 = Fish()
    # F1._set_gender(True)
    # F2 = Fish()
    # F2._set_gender(False)
    # F3 = Fish()
    # F3._set_gender(True)
    # F4 = Fish()
    # F4._set_gender(False)
    # B1 = Bear()
    # B1._set_gender(True)
    # B2 = Bear()
    # B2._set_gender(False)
    # B3 = Bear()
    # B1._set_gender(True)
    # B4 = Bear()
    # B4._set_gender(False)
    # Ecosysterm[13] = F4
    # Ecosysterm[24] = F1
    # Ecosysterm[35] = B4
    # Ecosysterm[40] = F3
    # Ecosysterm[49] = B1
    # Ecosysterm[74] = F2
    # Ecosysterm[85] = B3
    # Ecosysterm[99] = B2
    for j in range(100):
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()
        Fish().goto()

    for j in range(10):
        Bear().goto()
    from pprint import pprint
    pprint(Ecosysterm)

    for i in range(TERMS):
        """Cycle"""
        for j in Ecosysterm:
            if isinstance(j, Bear):
                B += 1
                j.M_S()
            elif isinstance(j, Fish):
                F += 1
                j.M_S()
        X.append(i)
        YB.append(B)
        YF.append(F)
        F = 0
        B = 0

    pprint(Ecosysterm)

    """Draw"""

    plt.plot(X, YB)
    plt.plot(X, YF)
    plt.title("Species change(bear and fish)")
    plt.xlabel('Cycle times')
    plt.ylabel('Bears or Fishes')
    plt.legend(["Bear", "Fish"])
    plt.show()
