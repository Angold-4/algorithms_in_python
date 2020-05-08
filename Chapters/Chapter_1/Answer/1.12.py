# Angold4 20200507 C1.1.12
from random import randrange


def choice(data):
    length = len(data)
    index = randrange(0, length, 1)
    return data[index]


if __name__ == "__main__":
    data = list(input())
    print(choice(data))
