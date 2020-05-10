# Angold4 20200509 C1.1.35
def main(num):
    import math
    p = 1 - math.pow((364/365), (num*(num-1)/2))
    return p


if __name__ == "__main__":
    print(main(23))
