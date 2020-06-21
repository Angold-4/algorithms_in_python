# Angold4 20200620 4.10
def n_log(n, i=0):
    """answer"""
    if n / 2 < 1:
        return i
    return n_log(n/2, i+1)


if __name__ == "__main__":
    print(n_log(129))
