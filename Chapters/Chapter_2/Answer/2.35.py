# 20200517 Angold4
import os


class Computer:

    def __init__(self, name):
        self._name = name
        self._storage = []
        self._addrstorage = []

    def get_name(self):
        return self._name

    def recieved(self, packages, path):
        if packages not in self._storage:
            self._storage.append(packages)
            self._addrstorage.append(path)
        else:
            print("Error,storage already have the same Duplicate package")

    def send_packages(self, aims, packages, path=''):
        try:
            aims.recieved(packages, path)
        except NameError:
            print("undefind name")

    def check(self):
        print("Here are the packages:")
        for i in range(len(self._storage)):
            print(self._storage[i], ':', self._addrstorage[i])

    def check_position(self, packages):
        j = 0
        if len(self._storage) == 0:
            return 'Empty!'
        for i in self._storage:
            if i == packages:
                addr = self._addrstorage[j]
                Path = os.path.join(addr, packages)
                return Path
            else:
                j += 1

    def read(self, packages):
        print("The file will be delete after open it")
        if packages in self._storage:
            for i in range(len(self._storage)):
                if self._storage[i] == packages:
                    _path = os.path.join(self._addrstorage[i], self._storage[i])
                    _file = open(_path)
                    del self._storage[i]
                    del self._addrstorage[i]
                    return _file.read()
        else:
            return "Not found"


if __name__ == "__main__":
    A = Computer('Alice')
    B = Computer('Bob')
    print(A.get_name())
    A.send_packages(B, '2.07.py', '/Users/Angold4/WorkSpace/algorithms_in_python/Chapters/Chapter_2/Answer')
    B.check()
    print(B.check_position('2.07.py'))
    print(B.read('2.07.py'))
    B.check()

"""

Alice
Here are the packages:
2.07.py : /Users/Angold4/WorkSpace/algorithms_in_python/Chapters/Chapter_2/Answer
/Users/Angold4/WorkSpace/algorithms_in_python/Chapters/Chapter_2/Answer/2.07.py
The file will be delete after open it
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

Here are the packages:

"""
