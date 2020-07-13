# Angold4 20200713 5.4
def __getitem__(self, k):
    """return element at index k"""
    min = -(self._n + 1)
    if not min <= k <= self._n:
        raise IndexError("invalid index")
    if min <= k < 0:
        return self._A[self._n + k]
