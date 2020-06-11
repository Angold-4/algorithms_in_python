# PS: About the answer from 2.10 - 2.33:Pleaz check the Notes of Chapter2
# 20200517 Angold4
import os
from matplotlib import pyplot as plt


class File:

    def __init__(self, filename, path=''):
        """make the path and check whether it is a correct path"""

        Path = os.path.join(path, filename)
        self._path = Path
        self._name = filename

        try:
            _tfile = open(self._path)
        except IOError as e:
            raise IOError("can't open the file or file not found", e)
        else:
            _tfile.close()

    def get_filename(self):
        return self._name

    def get_filepath(self):
        return self._path

    def get_content(self):
        _file = open(self._path)
        return _file.read()

    def get_lines(self):
        _c = 0
        _file = open(self._path)
        for i in _file:
            _c += 1
        _file.close()
        return _c

    def count_letter(self, letter):
        _c = 0
        _file = open(self._path)
        for i in _file.read():
            if i == letter:
                _c += 1
        _file.close()
        return _c

    def count_word(self, word):
        _c = 0
        _wordlist = []
        _symbol = (',', '.', ';', '*', '+', '-', '=', ' ', '(', ')', '\'', '\"', '\n')
        _file = open(self._path)
        for i in _file.read():
            if i in _symbol:
                _word = ''.join(_wordlist)
                if _word == word:
                    _c += 1
                _wordlist = []
            else:
                _wordlist.append(i)
        return _c

    def count_letters(self):
        _list = []
        _file = open(self._path)
        for i in _file.read():
            if i not in _list:
                _list.append(i)

        _dict = dict.fromkeys(_list, 0)
        _file = open(self._path)
        for i in _file.read():
            _dict[i] += 1
        xs = list(_dict.keys())
        ys = list(_dict.values())
        plt.bar(xs, ys)
        plt.show()

    def count_words(self):
        _wordlist = []
        _symbol = (',', '.', ';', ':', '*', '+', '-', '=', ' ', '(', ')',
                   '\'', '\"', '\n', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '1',
                   '2', '3', '4', '5', '6', '7', '8', '9', '0', '#', '!',
                   '<', '>', '/', '[', ']', '{', '}', '?', '%', '$')
        _file = open(self._path)
        _wordlists = []
        for i in _file.read():
            if i in _symbol:
                _word = ''.join(_wordlist)
                _wordlists.append(_word)
                _wordlist = []
            else:
                _wordlist.append(i)
        _dict = dict.fromkeys(_wordlists, 0)

        _file = open(self._path)
        for i in _file.read():
            if i in _symbol:
                _word = ''.join(_wordlist)
                _dict[_word] += 1
                _wordlist = []
            else:
                _wordlist.append(i)
        try:
            del _dict['']
        except KeyError:
            pass

        xs = list(_dict.keys())
        ys = list(_dict.values())
        plt.bar(xs, ys)
        plt.show()


"""Test"""

if __name__ == "__main__":
    F = File('2.36.py')
    print(F.get_content())
    print(F.get_lines())
    print(F.count_letter('p'))
    print(F.count_word('BCreditCard'))
    # F.count_letters()
    F.count_words()
