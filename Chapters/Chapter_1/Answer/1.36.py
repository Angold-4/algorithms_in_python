# Angold4 20200509 C1.1.36
def main():
    Str = input()
    List = Str.split()
    Dict = dict.fromkeys(List, 0)
    for i in List:
        Dict[i] += 1

    print(Dict)


if __name__ == "__main__":
    main()
