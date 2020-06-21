# Angold4 20200620 4.12
def mul(m, n):
    """answer"""
    if n == 1:
        return m
    return m + mul(m, n-1)


if __name__ == "__main__":
    print(mul(3, 3))
