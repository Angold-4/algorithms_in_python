# Angold4 20200507 C1.1.2
def is_even(k):
    length = len(bin(k))
    klist = list(bin(k))
    return klist[length-1] == '0'


if __name__ == "__main__":
    print(is_even(3))
