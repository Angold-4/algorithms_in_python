# Angold4 20200513


class Range:
    """A class that mimic's the built-in range class (Lazy evaluation)"""

    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("Step cannot be 0")

        if stop is None:
            start, stop = 0, start  # Special case for Range(n)

        self._length = max(0, (stop - start - 1 + step) // step)
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        """Return entry at index k"""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step


if __name__ == "__main__":
    R = Range(8, 140, 5)  # Just created a lightweight object
    print(R)  # An instance of a class with only a few behaviors
    print(R[3])  # It doesn't creat a real list

# <__main__.Range object at 0x10b1851c0>
# 23
