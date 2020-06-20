# Angold4 20200620 4.7
def tran(s):
    """answer"""
    if len(s) == 1:
        return int(s)
    else:
        return int(s[-1]) + 10*int(s[:-1])


if __name__ == "__main__":
    print(tran('2234'))
