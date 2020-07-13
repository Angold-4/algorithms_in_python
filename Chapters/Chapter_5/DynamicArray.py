# Angold4 20200709  DynamicArray
import ctypes  # It provides C compatible data types


class DynamicArray:
    """A dynamic array class akin to a simplified python list"""

    def __init__(self):
        """create an empty array"""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        """return element at index k"""
        min = -(self._n + 1)
        if not min <= k <= self._n:
            raise IndexError("invalid index")
        if min <= k < 0:
            return self._A[self._n + k]

    def append(self, obj):
        """add object to end of the array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """resize internal array to capacity c"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """return the new array with capacity c"""
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        """insert value at index k"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            """shifting subsequent values rightward"""
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """remove first occurence of value(or raise ValueError)"""
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self.A[j+1]
                    self._A[self._n - 1] = None
                    self._n -= 1
                    return
            raise ValueError('value not found')

    def __str__(self):
        """return the list string"""
        A = ''
        for i in range(self._n):
            A += str(i)
        return A


if __name__ == "__main__":
    A = DynamicArray()
    A.append(1)
    A.append(2)
    A.append(2)
    A.append(2)
    A.append(2)
    A.append(4)
    print(A[-1])
    print(A)
    B = (3 * ctypes.py_object)()
    C = 3 * ctypes.py_object
    print(B)
    print(C)
    """
    for b in B:
        print(b)
    ValueError: PyObject is NULL
    """
    B[0] = 1
    print(len(B))
    D = ctypes.py_object()
    print(D)
    """py_object(<NULL>)"""
