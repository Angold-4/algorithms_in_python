# Angold4 20200624 4.16
def reverse(s):
    """return the str that be reversed"""
    if len(s) == 0: # basic case
        return ""
    return reverse(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse('djiefiewie'))