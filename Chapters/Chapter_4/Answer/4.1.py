# Angold4 20200620 4.1
def normal_max(S):
    Max = S[0]
    for i in S:
        if i > Max:
            Max = i
    return Max


def find_max(S):
    """answer"""
    if len(S) == 1:
        return S[0]
    Max = S.pop()
    return max(Max, find_max(S))


if __name__ == "__main__":
    s = [1, 4, 4, 7, 3, 2, 20, 34, 90, 133, 113, 123, 5, 9, 293, 1]
    print(normal_max(s))
    print(find_max(s))

    """
    293
    293
    """
