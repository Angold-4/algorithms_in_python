# Angold4 20200513


class Progression:
    """Iterator producing a generic progression

    Defalut iterator produces the whole numbers 0, 1, 2,...
    """

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        """Update self._current to a new value"""

        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


"""Sub Classes"""


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current _advance method"""
        self._current += self._increment


class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current _advance method"""
        self._current *= self._base


class FobonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._pref = second - first

    def _advance(self):
        """Update current _advance method"""   # Return self._current as Answer
        self._pref, self._current = self._current, self._pref + self._current


"""Tests"""


if __name__ == "__main__":
    print("Default Progression:")
    Progression().print_progression(10)
    print("Arithmetic Progression with increment 5:")
    ArithmeticProgression(5).print_progression(10)
    print("Arithmetic Progression with increment 5 and start 2:")
    ArithmeticProgression(5, 2).print_progression(10)
    print("Geometric Progression with default base:")
    GeometricProgression().print_progression(10)
    print("Geometric Progression with base 3:")
    GeometricProgression(3).print_progression(10)
    print("Fobonacci Progression with dafault start values:")
    FobonacciProgression().print_progression(10)
    print("Fobonacci Progression with start values 4 and 6:")
    FobonacciProgression(4, 6).print_progression(10)


"""

Default Progression:
0 1 2 3 4 5 6 7 8 9
Arithmetic Progression with increment 5:
0 5 10 15 20 25 30 35 40 45
Arithmetic Progression with increment 5 and start 2:
2 7 12 17 22 27 32 37 42 47
Geometric Progression with default base:
1 2 4 8 16 32 64 128 256 512
Geometric Progression with base 3:
1 3 9 27 81 243 729 2187 6561 19683
Fobonacci Progression with dafault start values:
0 1 1 2 3 5 8 13 21 34
Fobonacci Progression with start values 4 and 6:
4 6 10 16 26 42 68 110 178 288

"""
