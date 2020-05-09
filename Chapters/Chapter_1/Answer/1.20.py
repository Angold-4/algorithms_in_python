# Angold4 20200509 C1.1.20
from random import randint


def shuffle(*data):
    repeat = []
    shuffle = []
    length = len(data)
    while True:
        number = randint(0, length-1)
        if number in repeat:
            if len(repeat) == length:
                return shuffle
        else:
            repeat.append(number)
            shuffle.append(data[number])


if __name__ == "__main__":
    print(shuffle(1, 2, 3, 4, 5))
