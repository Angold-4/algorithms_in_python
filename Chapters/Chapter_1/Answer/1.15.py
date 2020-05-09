# Angold4 20200509 C1.1.15
def main(*args):
    length = len(args)
    total = 0
    for i in range(length-1):
        a = args[i]
        for j in range(i+1, length):
            b = args[j]
            if a != b:
                total += 1
    if total == length*(length-1)/2:
        return True
    else:
        return False


if __name__ == "__main__":
    print(main(1, 2, 3, 5, 6))
