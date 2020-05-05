# Build in class
### Bulid in Class type

* The build in class that **can't** be changed:
    1. **bool**
    2. **int**
    3. **float**
    4. **tuple ( )**
    5. **str**
    6. **frozenset** -- the set that can't be changed



* The build in class that **can** be changed:
    1. **list [ ]**
    2. **dict { }**
    3. **set** -- the set that can be changed


### The Definition diff Between Can-Change and Can't-Change 

Each instance of a built-in class will have a fixed value when it is instantiated<br>If this value won't be changed in the subsequent operation 
it is a Can-Change-Instance<br>

**It is important that like when we instantiated a float type instance F<br>**
**If we change the value of F, The result is created as a new floating point instance F.<br>**
(The old F will being reserved as original)

```
# For Example:

alpha = [1,2,3] # List Object(Can Change)
beta = alpha
beta += [4.5]
beta = beta + [6,7]
# At that time alpha = [1,2,3,4,5] and beta = [1,2,3,4,5,6,7] 

'''-------------------------------------------------------------------'''

alpha = (1,2,3) # Tuple Object(Can't Change)
beta = alpha
beta += (4,5)
# At that time alpha still = (1,2,3) and beta = (1,2,3,4,5)

```

**Let me Explain:**
For the Can-change object like list, There are small difference between<br>
```beta += [4,5]``` and ```beta = beta += [4,5]```<br>The former opration won't reassign a new beta object(for Can-Change-Object)
But the latter will reassign a new beta object

Because of that the Tuple Object is a Can't change object. Every time we change it(Like beta += (4,5))<br> it won't change the original(=alpha)Tuple It will reassign a new beta Tuple object<br>That is why When we change beta Tuple We won't change Alpha<br>

### Why We Need Can't-Change Object

From [Stackoverflow](https://stackoverflow.com/questions/2174124/why-do-we-need-tuples-in-python-or-any-immutable-data-type):<br> 
```
$ python -mtimeit '["fee", "fie", "fo", "fum"]'
1000000 loops, best of 3: 0.432 usec per loop
$ python -mtimeit '("fee", "fie", "fo", "fum")'
10000000 loops, best of 3: 0.0563 usec per loop
```
> Immutable objects mean faster processing speed

