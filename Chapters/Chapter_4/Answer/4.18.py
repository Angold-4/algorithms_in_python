# Angold4 20200624 4.18
def vc(s):
    def v(s):
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if len(s) == 0:  # basic case
            return 0
        if s[0] in vowel:
            return 1 + v(s[1:])
        return v(s[1:])
    return v(s) > len(s)/2


if __name__ == "__main__":
    print(vc('dhashABCEIOUaeisou'))  # False
    print(vc('jslksjjk'))  # True