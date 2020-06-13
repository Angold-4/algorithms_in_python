#  Recursive Angold4 20200611
import Complexity


def factorial(n):
    if n == 0:  # Basic Condition
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print(factorial(10))  # 3628800
    fac = Complexity.Complexity(factorial)
    fac.set_first_element(1)
    fac.set_test_range(0, 200, 1)
    fac.statistics()
    fac.draw()
