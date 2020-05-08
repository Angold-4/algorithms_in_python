# Angold4 20200507 C1.1.1
def is_multiple(n, m):
    return(n % m == 0 and isinstance(n, int) and isinstance(m, int))


if __name__ == '__main__':
    print(is_multiple(3, 16))
