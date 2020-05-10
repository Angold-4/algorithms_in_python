# Angold4 20200509 C1.1.32 and C1.1.33
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divite(a, b):
    return a / b


def multiply(a, b):
    return a * b


def Divite(a, b):
    return a // b


def Balance(a, b):
    return a % b


def is_number(n):
    try:
        int(n)
        float(n)
        return True
    except ValueError:
        return False


def main():
    print("Caculator!!")
    Oprators = {'+': add, '*': multiply, '-': subtract, '/': divite, '//': Divite, '%': Balance}
    Number = []
    Oprator = []
    Answer = 0
    F = 0
    while True:
        Char = input()
        if is_number(Char):
            Char = float(Char)
            Number.append(Char)

        elif Char in Oprators:
            Oprator.append(Char)

        elif Char == "c":
            Number = []
            Oprator = []

        elif Char == "=":
            if len(Number) == len(Oprator)+1 and len(Number) >= 1:
                Answer = Number[0]
                for i in range(1, len(Number)):
                    F = Number[i]
                    Answer = Oprators[Oprator[i-1]](Answer, F)
                print(Answer)
                return Answer
        else:
            print("Error!")
            return False


if __name__ == "__main__":
    main()
