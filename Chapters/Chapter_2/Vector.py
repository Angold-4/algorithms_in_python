# Angold4 20200513


class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ == "__main__":
    """Test"""
    V1 = Vector(4)  # __init__
    V2 = Vector(4)
    V1[1] = 23  # __setitem__
    V2[-1] = 45
    V3 = V1 + V2  # __add__
    print(V1 == V2)  # __eq__
    print(V3[1])
    print(V1)
    print(V2)


"""
Test:
    False
    23
    <0, 23, 0, 0>
    <0, 0, 0, 45>


The Useage of __str__ attribute:
    if no __str__:
        V = Vector(4)
        print(V)
        <__main__.Vector object at 0x1082ca1c0>
    if has __str__:
        V = Vector(4)
        print(V)
        <0, 0, 0, 0>
"""
