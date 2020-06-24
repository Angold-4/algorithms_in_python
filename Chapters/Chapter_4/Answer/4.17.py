# Angold4 20200624 4.17
def ish(s):
    """based on func reverse"""
    def reverse(m):
        if len(m) == 0:
            return ''
        
        return reverse(m[1:]) + m[0]

    return reverse(s) == s


if __name__ == "__main__":
    print(ish('wsisw'))