# Angold4 20200509 C1.1.25
Listu = list(chr(k) for k in range(97, 123))
ListU = list(chr(k) for k in range(65, 91))


def main(char):
    Answer = []
    for i in char:
        if i in Listu + ListU:
            Answer.append(i)
    return "".join(Answer)


if __name__ == "__main__":
    print(main("jehfie,Lska.sda<S"))
