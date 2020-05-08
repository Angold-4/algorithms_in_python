# Angold4 20200507 C1.1.6
def is_even(k):
    length = len(bin(k))
    klist = list(bin(k))
    return klist[length-1] == '0'


def main(n):
    total = 0
    for i in range(1, n+1):
        if not is_even(i):
            total += i
    return total


if __name__ == "__main__":
    print(main(8))
