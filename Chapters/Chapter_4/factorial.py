#  Recursive Angold4 20200611
def factorial(n):
    if n == 0:  # Basic Condition
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print(factorial(10))  # 3628800
