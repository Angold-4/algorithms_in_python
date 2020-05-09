# Angold4 20200509 C1.1.16 1.17
def scale(data, factor):
    for val in data:
        val *= factor
        print(val)


if __name__ == "__main__":
    data = (1, 2, 3, 4, 6, 7)
    factor = 3
    scale(data, factor)
