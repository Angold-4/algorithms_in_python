# Angold4 20200513
from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """
    This abstract base class collections.sequence
    Which defines the common behavior of Python's list, str and tuple classes
    """

    @abstractmethod
    def __len__(self):
        """Must return the length of the Sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Must return the element at index j of the Sequence"""

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
            return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
            return k


class M(Sequence):
    pass


if __name__ == "__main__":
    M()

"""

Traceback (most recent call last):
  File "/Users/Angold4/WorkSpace/algorithms_in_python/Chapters/Chapter_2/Sequence.py", line 44, in <module>
    M()
TypeError: Can't instantiate abstract class M with abstract methods __getitem__, __len__

"""

"""Reference: https://blog.louie.lu/2017/07/28/你所不知道的-python-標準函式庫用法-03-abc/"""
