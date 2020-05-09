# Angold4 20200509 C1.1.22
def main(TA, TB):
    Answer = []
    if len(TA) != len(TB) or len(TA) == 0:
        raise ValueError("The Length of Tuple A and Tuple B must be the same!")
    else:
        length = len(TA)
        for i in range(length):
            Answer.append(TA[i]*TB[i])
        return Answer


if __name__ == "__main__":
    TA = (1, 2, 3, 4, 5, 6)
    TB = (2, 4, 6, 8, 10, 12)
    print(tuple(main(TA, TB)))
