# Angold 4 20200713 5.16
import ctypes


def pop(self):
    """pop the last element"""
    if self._n <= (self._capacity / 4):
        self._capacity = (self._capacity / 2)
        C = self._make_array(self._capacity)
        for k in range(self._n):
            C[k] = self._A[k]

        self._A = C
    D = self._A[self._n-1]
    self._A[self._n-1] = ctypes.py_object()
    self._n -= 1
    return D
