# Angold4 20200509 C1.1.28
from math import pow


def norm(v, p):
    V = 0
    for i in v:
        V += i**p
    return pow(V, 1/p)


if __name__ == "__main__":
    List = [3, 4]
    print(norm(List, 2))
