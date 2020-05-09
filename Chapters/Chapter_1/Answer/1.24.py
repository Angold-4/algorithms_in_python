# Angold4 20200509 C1.1.23
def main(String):
    List = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    Total = 0
    for i in String:
        if i in List:
            Total += 1
    return Total


if __name__ == "__main__":
    string = input()
    print(main(string))
