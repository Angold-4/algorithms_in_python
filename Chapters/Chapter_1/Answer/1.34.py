# Angold4 20200509 C1.1.34
def main():
    i = 0
    j = 0
    while True:
        a = input()
        if a == "I will never spam my friends again.":
            i += 1
            if i == 10:
                return True

        elif j == 8:
            return False

        else:
            j += 1


if __name__ == "__main__":
    main()
