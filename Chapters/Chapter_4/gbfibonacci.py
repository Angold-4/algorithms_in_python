#  20200613 Angold4
import Complexity


def bad_fibonacci(n):
    """return the No.n fibonacci number

    it is bad code
    """
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-1) + bad_fibonacci(n-2)


def good_fibonacci(n):
    """return pair of fibonacci numbers, F(n) and F(n-1)

    it is good code:)
    """
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return(a+b, a)


if __name__ == "__main__":

    from time import time

    """good fibonacci"""
    start_time = time()
    print(bad_fibonacci(40))
    end_time = time()
    print(start_time - end_time)

    """bad fibonacci"""
    start_time = time()
    print(good_fibonacci(40))
    end_time = time()
    print(start_time - end_time)

    """
    102334155
    -32.8236978054
    (102334155, 63245986)
    -1.90734863281e-05
    """

    bf = Complexity.Complexity(bad_fibonacci)
    bf.set_first_element(1)
    bf.set_test_range(0, 20, 1)
    bf.average()
    bf.draw()

    gf = Complexity.Complexity(good_fibonacci)
    gf.set_first_element(1)
    gf.set_test_range(0, 20, 1)
    gf.average()
    gf.draw()

    Complexity.Compare(bf, gf)
