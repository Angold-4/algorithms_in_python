# Angold4 20200509 C1.1.27
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == 0:
        yield k


def fibonacci():
    a = 0
    b = 1
    while a < 100:
        yield a
        future = a + b
        a = b
        b = future


def factorsW(n):
    k = 1
    List = []
    while k * k < n:
        if n % k == 0:
            yield k
            List.append(n // k)
        k += 1
    if k * k == 0:
        yield k
    for s in List[::-1]:
        yield s


if __name__ == "__main__":
    for i in factors(100):
        print(i)
    for j in fibonacci():
        print(j)
    for s in factorsW(100):
        print(s)
