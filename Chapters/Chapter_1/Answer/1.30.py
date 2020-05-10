# Angold4 20200509 C1.1.30
def main():
    char = int(input())
    i = 1
    while True:
        char /= 2
        i += 1
        if char // 2 < 2:
            print(i)
            break


if __name__ == "__main__":
    main()
