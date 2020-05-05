# Python Special


<!-- vim-markdown-toc GFM -->

* [Iterator:](#iterator)
* [Generator:](#generator)
    * [Two examples:](#two-examples)
* [Why we need Iterator and Generator:](#why-we-need-iterator-and-generator)

<!-- vim-markdown-toc -->

### Iterator:
**We can notice that in python, many types of objects are interable<br>**
**Such as list, tuple or even set, str, dict...<br>**

> Many data are "containers"; they contain many other types of elements.
> When actually using containers, we often need to get the elements one by one. The process of getting elements one by one is "iterating"

```python

print(isinstance([], Iterable))  # True: list is iterable
print(isinstance({}, Iterable))  # True: dic is iterable
print(isinstance((), Iterable))  # True: tuple is iterable
print(isinstance(set(), Iterable))  # True set is iterable
print(isinstance('', Iterable))  # True str is iterable

currPath = os.path.dirname(os.path.abspath(__file__))
with open(currPath+'/model.py') as file:
    print(isinstance(file, Iterable)) # true

```

**In Python We can treat every class which has ```__iter__``` attribute as a interable object<br>**
```python
class IterObj:
    
    def __iter__(self):
        return self
it = IterObj() 
print(isinstance(it, Iterable))  # True
print(isinstance(it, Iterator))  # False
print(isinstance(it, Generator)) # False

```
**In Python if a class has both ```__iter__```and```__next__```attributes. we can call it an Iterator**

```python
class IterObj:

    def __init__(self):
        self.a = [3, 5, 7, 11, 13, 17, 19]

        self.n = len(self.a)
        self.i = 0

    def __iter__(self):
        return iter(self.a)

    def __next__(self):
        while self.i < self.n:
            v = self.a[self.i]
            self.i += 1
            return v
        else:
            self.i = 0
            raise StopIteration()
    it = IterObj()
    print(isinstance(it, Iterable)) # True
    print(isinstance(it, Iterator)) # True
    print(isinstance(it, Generator)) # False
    print(hasattr(it, "__iter__")) # True
    print(hasattr(it, "__next__")) # True


```


**As a interator. We can use ```next()``` build-in method to call the next elements:<br>**


```python

In [28]: a = [1,2,3,4,5]

In [29]: b = iter(a)

In [30]: next(b)
Out[30]: 1

In [31]: next(b)
Out[31]: 2

In [32]: next(b)
Out[32]: 3

In [33]: next(b)
Out[33]: 4

In [34]: next(b)
Out[34]: 5

```

**In this example: Calling ```iter()``` method on an instance will produce an instance of list_iterator.<br> 
The iterator will not store a copy of the elements of its own list.<br> Instead, it will save the current index of the original list and point the index to the next element**

**We can understand in this way: In Python: When we call the for or while loop.<br>**
**The nature behind this is that it will call the ```__iter__``` method in our iterable object<br>**
**then in this method. Will call the iter() method which create a instance(our object's iterator)<br>**
**And then. The for-loop will call the ```next()``` method of our iterator instance**



### Generator:

**
Unlike ordinary functions, after the generator function is called, the code in its function body is not executed immediately, but a generator-iterator is returned. When the returned generator calls a member method, the code in the corresponding generator function is executed.**
#### Two examples:

```python

def factors(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
        return results

```
**We can use generator func achieve the same goal:**
```python

def factors(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k

```

****

```python

def square():
    for x in range(4):
        yield x ** 2
square_gen = square()
for x in square_gen:
    print(x)

```
**This square function is equal to:**
```python

genitor = square_gen.__iter__()
while True:
    x = geniter.__next__()
    print(x)

```


**If you still don't understand generator functions, you can generally understand it this way:**

* At the beginning of the function, add ```result = list()```
* Replace each yield expression ```yield expr``` with ```result.append(expr)```
* At the end of the function, add ```return result```.



### Why we need Iterator and Generator:

**
In many cases, we just need to access the elements in the container one by one.<br>Most of the time, we don't need to "get all the elements in the container in one go".<br> For example, there are two ways to access the first 5 elements in the container in sequence:**
1. Get all the elements in the container, and then take out the first 5;
2. From the beginning, iterate over the elements in the container one by one, and stop after iterating over 5 elements.

**Obviously, if the number of elements in the container is very large (for example, 10 ^ 8), or the volume of the elements in the container is very large, then the latter solution can save huge time and space overhead.
**


**reference:**
*[Liam](https://liam.page/2017/06/30/understanding-yield-in-python/)*
*[Juejin](https://juejin.im/post/5ccafbf5e51d453a3a0acb42)*




