# Angold4 20200509 C1.1.29
from random import randint


def main():
    print("Don't place repeated characters!")
    char = input()
    Lchar = list(char)
    length = len(Lchar)
    Total = 1
    for i in range(1, length+1):
        Total *= i
    Answer = []
    List = []
    while True:
        while True:
            i = randint(0, length-1)
            if Lchar[i] not in Answer and len(Answer) < length:
                Answer.append(Lchar[i])
            if len(Answer) == length:
                break
        answer = "".join(Answer)
        Answer = []
        if answer not in List:
            List.append(answer)
            print(answer)
        if len(List) >= Total:
            break


if __name__ == "__main__":
    main()
