#  Angold4 20200613
import Complexity


def normal_power(x, n):
    """Complexity: O(n)"""
    if n == 0:
        return 1
    else:
        return x * normal_power(x, n-1)


def power(x, n):
    """Complexity: O(log n)"""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


if __name__ == "__main__":

    from time import time

    start_time = time()
    print(power(5, 24))
    end_time = time()
    print(start_time - end_time)

    start_time = time()
    print(normal_power(5, 24))
    end_time = time()
    print(start_time - end_time)
    """
    59604644775390625
    -1.0967254638671875e-05
    59604644775390625
    -7.152557373046875e-06
    """

    np = Complexity.Complexity(normal_power)
    np.set_first_element(2)
    np.set_second_element(1)
    np.set_test_range(1, 300, 1)
    np.average(1000)
    np.draw()

    p = Complexity.Complexity(power)
    p.set_first_element(2)
    p.set_second_element(1)
    p.set_test_range(1, 300, 1)
    p.average(1000)
    p.draw()

    Complexity.Compare(np, p)
