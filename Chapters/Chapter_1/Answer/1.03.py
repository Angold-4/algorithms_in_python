# Angold4 20200507 C1.1.3
def minmax(*data):
    max = -999999999
    min = 999999999
    print(data)
    for i in data:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min


if __name__ == "__main__":
    print(minmax(1, 2, 3, 4, 5, 6, 7))
