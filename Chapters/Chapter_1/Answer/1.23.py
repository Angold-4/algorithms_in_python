# Angold4 20200509 C1.1.23
def Check_Overflow(List, index):
    a = []
    try:
        for i in range(index):
            a.append(List[i])
            print(a)
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")


if __name__ == "__main__":
    List = [1, 2, 3, 4, 5]
    Check_Overflow(List, 8)
