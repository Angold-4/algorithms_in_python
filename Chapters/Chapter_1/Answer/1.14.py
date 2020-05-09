# Angold4 20200509 C1.1.14
def main(*args):
    length = len(args)
    for i in range(length):
        a = args[i]
        for j in range(i + 1, length):
            b = a*args[j]
            if b % 2 != 0 and b != a:
                return True


if __name__ == "__main__":
    print(main(2, 2, 2))
