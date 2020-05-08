# Angold4 20200507 C1.1.4
def main(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum


if __name__ == "__main__":
    print(main(8))
