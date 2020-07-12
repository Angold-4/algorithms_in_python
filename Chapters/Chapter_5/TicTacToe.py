# Angold4 20200712
"""
Before we start the TicTacToe Game
Let's check the right way to create a Matrix
"""

"""
In [11]: lb = [[1, 0, 0] * 3] * 3]

In [12]: lb
Out[12]:
[[1, 0, 0, 1, 0, 0, 1, 0, 0],
 [1, 0, 0, 1, 0, 0, 1, 0, 0],
 [1, 0, 0, 1, 0, 0, 1, 0, 0]]

In [13]: id(lb)
Out[13]: 140322539003520

In [14]: id(lb[0])
Out[14]: 140322536112256

In [15]: id(lb[1])
Out[15]: 140322536112256

In [16]: id(lb[2])
Out[16]: 140322536112256

In [17]: lb[2][1] = 3

In [18]: lb
Out[18]:
[[1, 3, 0, 1, 0, 0, 1, 0, 0],
 [1, 3, 0, 1, 0, 0, 1, 0, 0],
 [1, 3, 0, 1, 0, 0, 1, 0, 0]]

In [19]: lc = [[0] * 3 for j in range(3)]

In [20]: lc
Out[20]: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

In [21]: lc[1]
Out[21]: [0, 0, 0]

In [22]: id(lc[1])
Out[22]: 140322539637120

In [23]: id(lc[0])
Out[23]: 140322540272448

In [24]: lc[0][1] = 5

In [25]: lc
Out[25]: [[0, 5, 0], [0, 0, 0], [0, 0, 0]]
"""


class TicTacToe:
    """management of a tic-tac-toe game (does not do strategy)"""

    def __init__(self):
        """start a new game"""
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        """put an X or O mark at position (i, j) for next player's turn"""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position")
        if self._board[i][j] != ' ':
            raise ValueError("Board position occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        """check whether the board configuration is win for the given number"""
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][1] == board[1][0] == board[2][0] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        """return mark of winning player, or None to indicate a tie"""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        """return string representation of current game board"""
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)


if __name__ == "__main__":
    game = TicTacToe()
    game.mark(1, 1)
    game.mark(0, 2)
    game.mark(2, 2)
    game.mark(0, 0)
    game.mark(0, 1)
    game.mark(2, 1)
    game.mark(1, 2)
    game.mark(1, 0)
    game.mark(2, 0)
    print(game)
    winner = game.winner()
    if winner is None:
        print('Tie')
    else:
        print(winner, 'wins')

    """
    O|X|O
    -----
    O|X|X
    -----
    X|O|X
    Tie
    """
