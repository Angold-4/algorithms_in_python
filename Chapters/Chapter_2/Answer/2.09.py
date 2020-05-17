# Angold4 20200517 2.09 and 2.10.py and 2.12.py and 2.14.py
import sys; sys.path.append('..')  # Change the relative path
from Vector import Vector


class SVector(Vector):
    def __init__(self, *args):
        if len(args) == 1:
            d = args[0]
            self._coords = [0] * d
        else:
            self._coords = list(args)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] - self[j]
        return result

    def __neg__(self):
        for j in range(len(self)):
            self[j] *= -1
        return self

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            for j in range(len(self)):
                self[j] *= other
            return self
        elif len(other) == len(self):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other[j]
            return result
        else:
            raise ValueError("dimensions not agree or not a number")

    def __rmul__(self, other):
        if type(other) is int or type(other) is float:
            for j in range(len(self)):
                self[j] *= other
        elif len(other) == len(self):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other[j]
            return result
        else:
            raise ValueError("dimensions not agree or not a number")


"""Test"""

if __name__ == "__main__":
    A = SVector(5)
    B = SVector(1, 2, 3, 4, 5)
    print(A)
    print(B)
    C = -B
    print(C)
    print(A - B)
    print(B*C)
    A = 2
    print(B*A)

"""

<0, 0, 0, 0, 0>
<1, 2, 3, 4, 5>
<-1, -2, -3, -4, -5>
<-1, -2, -3, -4, -5>
<1, 4, 9, 16, 25>
<-2, -4, -6, -8, -10>

"""
