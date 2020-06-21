# Angold4 20200620 4.15
def aset(L):
    """answer"""
    if L == []:
        return [[]]
    x = aset(L[1:])
    return x + [[L[0]] + y for y in x]


if __name__ == "__main__":
    lsts = [1, 2]
    print(aset(lsts))

    """
    In [86]: [[]] + [[1]]
    Out[86]: [[], [1]]

    In [87]: [[]] + [[1]+[]]
    Out[87]: [[], [1]]

    In [88]: [[]] + [[1]+[2]]
    Out[88]: [[], [1, 2]]
    """
