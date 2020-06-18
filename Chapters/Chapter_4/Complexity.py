#  Angold4 20200613
"""

A Program that help us do Complexity analysis
To Use it. Just import Complexity;-) """
from time import time
from functools import wraps

t = []
avlist = []


class Complexity:
    def __init__(self, fun):
        self.listx = []
        self.fun = fun
        self.el = [None]*3

    def set_first_element(self, ele):
        self.el[0] = ele

    def set_second_element(self, ele):
        self.el[1] = ele

    def set_third_element(self, ele):
        self.el[2] = ele

    def set_test_range(self, elenumber, to, step):
        if self.el[elenumber] is None:
            raise ValueError("please set the first number of given range")
        if elenumber >= 3 or self.el[elenumber] >= to:
            raise ValueError
        else:
            self.re = [elenumber, to, step]

    def ctime(func):
        @wraps(func)
        def wrapper(a1, a2, a3, a4):
            start_time = time()
            func(a1, a2, a3, a4)
            end_time = time()
            global t
            t.append(end_time - start_time)
        return wrapper

    @ctime
    def caculate_time(self, p1=None, p2=None, p3=None):  # TODO:add algorithms
        """fool method"""
        if p3 is None and p2 is None:
            self.fun(p1)
        elif p3 is not None and p2 is not None and p1 is not None:
            self.fun(p1, p2, p3)
        else:
            self.fun(p1, p2)

    def statistics(self):  # TODO:add algorithms
        """fool method"""
        for e in range(self.el[self.re[0]], self.re[1], self.re[2]):
            # self.listx.append(e)
            if self.re[0] == 0:
                self.caculate_time(e, self.el[1], self.el[2])
            elif self.re[0] == 1:
                self.caculate_time(self.el[0], e, self.el[2])
            elif self.re[0] == 2:
                self.caculate_time(self.el[0], self.el[1], e)
            else:
                raise ValueError("please call func 'set_test_range'")

    def average(self, times=2):
        """get a more accurate value"""
        for i in range(times):
            self.statistics()
            global t, avlist
            length = len(t)
            avlist.append(t)
            t = []

        total_list = []

        for l in range(length):
            total_list.append([])

        for j in range(times):
            """per time"""
            for i in range(length):
                total_list[i].append(avlist[j][i])

        """calculate"""
        ylist = []
        avlist = []
        for a in total_list:
            avg = 0
            for b in a:
                avg += b
            ylist.append(avg/times)
        self.listy = ylist

        for e in range(self.el[self.re[0]], self.re[1], self.re[2]):
            self.listx.append(e)

    def draw(self):
        if not self.listy and not self.listx:
            raise ValueError("before draw func please call func 'average'")

        else:
            from matplotlib import pyplot as plt
            plt.plot(self.listx, self.listy)
            plt.xlabel("arguments")
            plt.ylabel("run time")
            plt.title("Complexity Analysis")
            plt.show()


def Compare(*args):
    from matplotlib import pyplot as plt
    lstx = []
    Tlist = []
    if len(args) == 0:
        raise ValueError("please enter the Complexity obj as arguments")
    for a in args:
        if not a.listy:
            """not do draw"""
            a.draw()
        Tlist.append(a.fun)
        for i in range(1, len(a.listy)+1):
            lstx.append(i)

        plt.plot(lstx, a.listy)
        """clear for the next"""
        lstx = []

    plt.title("Complexity Compare")
    plt.xlabel("arguments")
    plt.ylabel("run time")
    plt.legend(Tlist)
    plt.show()


if __name__ == "__main__":
    def Test1(a1, a2):
        return a1, a2

    def Test2(a1):
        for i in range(a1):
            a1 += i

    def Test3(a1):
        for i in range(a1):
            a1 *= i

    Complexity1 = Complexity(Test1)
    Complexity1.set_first_element(1)
    Complexity1.set_second_element(3)
    Complexity1.set_test_range(0, 5, 1)
    Complexity1.average()
    Complexity1.draw()
    Complexity2 = Complexity(Test2)
    Complexity2.set_first_element(1)
    Complexity2.set_test_range(0, 5, 1)
    Complexity2.average()
    Complexity2.draw()
    Complexity3 = Complexity(Test3)
    Complexity3.set_first_element(1)
    Complexity3.set_test_range(0, 5, 1)
    Complexity3.average()
    Complexity3.draw()

    Compare(Complexity1, Complexity2, Complexity3)
