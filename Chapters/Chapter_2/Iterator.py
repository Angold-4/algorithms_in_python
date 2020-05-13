# Angold4 20200513


class SequenceInterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an interator must return itself as an iterator"""
        return self


if __name__ == "__main__":
    Iterator = SequenceInterator([1, 2, 3, 4, 5])
    print(next(Iterator))
