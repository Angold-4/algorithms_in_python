# Angold4 20200518 2.38.py
import sys; sys.path.append('..')  # Change the relative path
from PCreditCard import PredatoryCreditCard


class Book:

    def __init__(self, name, author, price, source):
        self._name = name
        self._author = author
        self._price = price
        self._source = source

    def __add__(self, other):
        Answer = 0
        currency = ["$", "$", ":"]
        strnumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
        cilist = []
        cjlist = []
        ilist = []
        jlist = []
        for i in self._price:
            """i --> self"""
            if i in currency:
                cilist.append(i)
            elif i in strnumber:
                ilist.append(i)

        if type(other) is int or type(other) is float:
            """j --> other"""
            jnumber = other
        else:
            for j in other._price:
                if j in currency:
                    cjlist.append(j)
                elif j in strnumber:
                    jlist.append(j)
            jnumber = float(''.join(jlist))

        inumber = float(''.join(ilist))
        Answer = inumber + jnumber
        if cilist == cjlist:
            return ''.join(cilist)+str(Answer)
        else:
            return Answer

    def __radd__(self, other):
        Answer = 0
        currency = ["$", "$", ":"]
        strnumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
        cilist = []
        cjlist = []
        ilist = []
        jlist = []
        for i in self._price:
            """i --> self"""
            if i in currency:
                cilist.append(i)
            elif i in strnumber:
                ilist.append(i)

        if type(other) is int or type(other) is float:
            """j --> other"""
            jnumber = other
        else:
            for j in other._price:
                if j in currency:
                    cjlist.append(j)
                elif j in strnumber:
                    jlist.append(j)
            jnumber = float(''.join(jlist))

        inumber = float(''.join(ilist))
        Answer = inumber + jnumber
        if cilist == cjlist:
            return ''.join(cilist)+str(Answer)
        else:
            return Answer


class BookStore:

    def __init__(self):
        self._bookdict = {}
        self._pricedict = {}
        self._sourcedict = {}
        self._book = {}
        self._viplist = []

    def check(self, bookname):
        return self._bookdict.__contains__(bookname)

    def find_price(self, bookname):
        try:
            return self._pricedict[bookname]
        except IndexError as e:
            print("sorry, we don't apply:", bookname, e)

    def find_author(self, bookname):
        try:
            return self._bookdict[bookname]
        except IndexError as e:
            print("sorry, we don't apply:", bookname, e)

    def _append(self, book):
        if isinstance(book, Book):
            if book._name not in self._bookdict:
                _pricedict = {book._name: book._price}
                _authordict = {book._name: book._author}
                _sourcedict = {book._name: book._source}
                self._bookdict.update(_authordict)
                self._pricedict.update(_pricedict)
                self._sourcedict.update(_sourcedict)
                self._book[book._name] = book
            else:
                pass
        else:
            print("Sorry, we only accept books certified by the bookstore")

    def _addcard(self, customer, bank, acnt, limit, apr):
        self._creditcard = PredatoryCreditCard(customer, bank, acnt, limit, apr)

    def _remove(self, bookname):
        if bookname in self._bookdict:
            self._bookdict.pop(bookname)
            self._pricedict.pop(bookname)
            self._sourcedict.pop(bookname)
        else:
            print("name", bookname, "not found")

    def _bevip(self, person):
        if isinstance(person, Person):
            if person in self._viplist:
                print(person._gender, person._name, "You are already our VIP member")
            else:
                if person._creditcard and self._creditcard:
                    person._creditcard.charge(50)
                    self._creditcard.make_payment(50)
                    self._viplist.append(person)
                else:
                    print("Error! Card not found")

    def check_wallet(self):
        if self._creditcard:
            print("Name:", self._creditcard.get_customer())
            print("Bank:", self._creditcard.get_bank())
            print("Account:", self._creditcard.get_account())
            print("Balance:", self._creditcard.get_balance())
            print("Limit:", self._creditcard.get_limit())
        else:
            print("no card yet.you can call '_addcard()' method to add a card")

    def buy(self, person, bookname):
        strnumber = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
        ilist = []
        Answer = 0
        if isinstance(person, Person) and bookname in self._bookdict:
            price = self._pricedict[bookname]
            for i in price:
                if i in strnumber:
                    ilist.append(i)
            Answer = float(''.join(ilist))
            if person in self._viplist:
                Answer *= 0.9
        else:
            print("invalid bookname or person")
            return False

        print("You need to Pay: $", Answer)
        print("Processing...")
        person._creditcard.charge(Answer)
        self._creditcard.make_payment(Answer)
        person._bookdict[bookname] = self._sourcedict[bookname]
        print("Finished! :-)")

    def add_shoppinglist(self, person, bookname):
        if bookname in self._bookdict and isinstance(person, Person):
            person._shoppinglist.append(bookname)
        else:
            print("invalid bookname or person")

    def settlement(self, person):
        Total = 0
        if isinstance(person, Person):
            for i in person._shoppinglist:
                Book = self._book[i]
                Total = Total + Book
                person._bookdict[i] = self._sourcedict[i]
            if person in self._viplist:
                Total *= 0.85

            print("You need to Pay: $", Total)
            print("Processing...")
            person._creditcard.charge(Total)
            self._creditcard.make_payment(Total)
            person._shoppinglist = []
            print("Finished! :-)")


class Person:

    def __init__(self, name, gender):
        MS = ['Mr.', 'Miss.']
        self._name = name
        self._bookdict = {}
        self._shoppinglist = []
        try:
            self._gender = MS[gender]
        except IndexError:
            print("gender must be 0(Male) or 1(Female)")

    def _addcard(self, customer, bank, acnt, limit, apr):
        self._creditcard = PredatoryCreditCard(customer, bank, acnt, limit, apr)

    def check_wallet(self):
        if self._creditcard:
            print("Name:", self._creditcard.get_customer())
            print("Bank:", self._creditcard.get_bank())
            print("Account:", self._creditcard.get_account())
            print("Balance:", self._creditcard.get_balance())
            print("Limit:", self._creditcard.get_limit())
        else:
            print("no card yet.you can call '_addcard()' method to add a card")

    def check_order(self):
        return self._bookdict


"""Test"""
if __name__ == "__main__":

    Books = {'When Breath Becomes Air': 'Paul Kalanithi',
             'Sapiens: A Brief History of Humankind': 'Yuval Noah Harari',
             'Surely You’re Joking, Mr. Feynman!': 'Richard P. Feynman',
             'Manual for Living': 'Epictetus',
             'Meditations': 'Marcus Aureliusk',
             'A Brief History of Time': 'Stephen Hawking',
             'This is Water': 'David Foster Wallace'}

    Prices = {'When Breath Becomes Air': '$:12.16',
              'Sapiens: A Brief History of Humankind': '$:12.86',
              'Surely You’re Joking, Mr. Feynman!': '$:9.04',
              'Manual for Living': '$:2.99',
              'Meditations': '$:2.99',
              'A Brief History of Time': '$:12.96',
              'This is Water': '$:9.99'}

    Sources = {'When Breath Becomes Air': 'https://www.amazon.com/When-Breath-Becomes-Paul-Kalanithi/dp/081298840X',
               'Sapiens: A Brief History of Humankind': 'https://www.amazon.com/Sapiens-Humankind-Yuval-Noah-Harari/dp/0062316095',
               'Surely You’re Joking, Mr. Feynman!': 'https://www.amazon.com/Surely-Feynman-Adventures-Curious-Character/dp/0393316041',
               'Manual for Living': 'https://www.amazon.com/Manual-Living-Little-Wisdom-Francisco/dp/0062511114',
               'Meditations': 'https://www.amazon.com/Meditations-Marcus-Aurelius/dp/1503280462',
               'A Brief History of Time': 'https://www.amazon.com/Brief-History-Time-Stephen-Hawking/dp/0553380168',
               'This is Water': 'https://www.amazon.com/This-Water-Delivered-Significant-Compassionate/dp/0316068225'}

    A = Book('A', 'a', '$:89', 'amazon')
    B = Book('B', 'b', '$:68.9', 'amazon')
    print(A + B)  # $:157.9
    print(78.9 + A)  # 167.9

    B1 = Book('When Breath Becomes Air', 'Paul Kalanithi', '$:12.16', 'https://www.amazon.com/When-Breath-Becomes-Paul-Kalanithi/dp/081298840X')
    B2 = Book('This is Water', 'David Foster Wallace', '$:9.99', 'https://www.amazon.com/This-Water-Delivered-Significant-Compassionate/dp/0316068225')
    B3 = Book('Meditations', 'Marcus Aureliusk', '$:2.99', 'https://www.amazon.com/Meditations-Marcus-Aurelius/dp/1503280462')
    B4 = Book('A Brief History of Time', 'Stephen Hawking', '$:12.96', 'https://www.amazon.com/Brief-History-Time-Stephen-Hawking/dp/0553380168')
    B5 = Book('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', '$:12.86', 'https://www.amazon.com/Sapiens-Humankind-Yuval-Noah-Harari/dp/0062316095')

    bookstore = BookStore()
    bookstore._append(B1)
    bookstore._append(B2)
    bookstore._append(B3)
    bookstore._append(B4)
    bookstore._append(B5)
    # print(bookstore._bookdict)
    bookstore._addcard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, 0.0825)

    Peter = Person('Peter', 0)
    Peter._addcard('Peter Wong', 'California Savings', '5391 0375 9387 6789', 10000, 0.0725)
    Ray = Person('Ray', 1)
    Ray._addcard('Raybb', 'California Savings', '5391 0375 9387 0131', 9000, 0.0736)
    bookstore._bevip(Ray)
    bookstore._bevip(Ray)


    bookstore.buy(Peter, 'Meditations')
    Peter.check_wallet()
    print(Peter.check_order())
    bookstore.check_wallet()
    print()

    bookstore.add_shoppinglist(Peter, 'This is Water')
    bookstore.add_shoppinglist(Peter, 'When Breath Becomes Air')
    bookstore.add_shoppinglist(Peter, 'A Brief History of Time')
    bookstore.settlement(Peter)
    Peter.check_wallet()
    bookstore.check_wallet()
    print()

    bookstore.add_shoppinglist(Ray, 'This is Water')
    bookstore.add_shoppinglist(Ray, 'When Breath Becomes Air')
    bookstore.add_shoppinglist(Ray, 'A Brief History of Time')
    bookstore.add_shoppinglist(Ray, 'Meditations')
    bookstore.settlement(Ray)
    Ray.check_wallet()
    bookstore.check_wallet()

"""

Miss. Ray You are already our VIP member
You need to Pay: $ 2.99
Processing...
Finished! :-)
Name: Peter Wong
Bank: California Savings
Account: 5391 0375 9387 6789
Balance: 2.99
Limit: 10000
{'Meditations': 'https://www.amazon.com/Meditations-Marcus-Aurelius/dp/1503280462'}
Name: John Bowman
Bank: California Savings
Account: 5391 0375 9387 5309
Balance: -52.99
Limit: 2500

You need to Pay: $ 35.11
Processing...
Finished! :-)
Name: Peter Wong
Bank: California Savings
Account: 5391 0375 9387 6789
Balance: 38.1
Limit: 10000
Name: John Bowman
Bank: California Savings
Account: 5391 0375 9387 5309
Balance: -88.1
Limit: 2500

You need to Pay: $ 32.385
Processing...
Finished! :-)
Name: Raybb
Bank: California Savings
Account: 5391 0375 9387 0131
Balance: 82.38499999999999
Limit: 9000
Name: John Bowman
Bank: California Savings
Account: 5391 0375 9387 5309
Balance: -120.48499999999999
Limit: 2500

"""
