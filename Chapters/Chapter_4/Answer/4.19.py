# Angold4 20200624 4.19
def oae(l):
    def oe(l):
        """do grouping"""
        if len(l) == 0:
            return [[], []]
        b = oe(l[1:])
        if l[0] % 2 == 0:
            b[0].append(l[0])
        else:
            b[1].append(l[0])
        return b
    return oe(l)[0] + oe(l)[1]
    

if __name__ == "__main__":
    print(oae([1, 3, 5, 4, 8, 10, 19]))