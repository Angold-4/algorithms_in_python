#  Position elements in an ordered array(Normal Way) Angold4 20200611
import Complexity
"""
                        Binary Search
First thing we need to know is that Every time we do binary search
the number of candidate entry to be found is given and is == high - low + 1

Another important thing is that After Every recursive call:
            this number n is reduced by half

Specifically there are two Conditions:
    1.n = (mid-1)-low+1 = |_(low + high) / 2_| - low <= (high-low+1)/2
    2.n = high-(mid+1)+1 = high - |_(low + high)_| / 2 <= (high-low+1)/2

From these two Conditions We can find out that:
assuming first time the given number is high-low+1 = n
After first binary search the remaining number are at most half(n/2)
After second binary search the remaining number are at most half(n/4)
...............
After Maximum binary search(j) the remaining <= n/(2^j)


For the Worst Condition like there is no match in the data.
Assuming this number is r. So at that time: We have (n/2^r < 1)
=>  r > log n  =>  r = |_log n_| + 1  =>  time Complexity is O(log n)

"""


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)


def normal_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i

    return False


if __name__ == "__main__":

    from time import time

    data = [1, 2, 3, 5, 7, 8, 9, 11, 13, 16, 19, 25, 39, 109, 111, 123, 135,
            190, 202, 550, 1022, 12123, 34594, 68994, 111234]

    target = 111234

    """binary_search"""
    start_time = time()
    print(binary_search(data, target, 0, 24))
    end_time = time()
    print(start_time - end_time)

    """normal_search"""
    start_time = time()
    print(normal_search(data, target))
    end_time = time()
    print(start_time - end_time)

    """
    24
    -1.2874603271484375e-05
    24
    -5.0067901611328125e-06
    """

bs = Complexity(binary_search)
ns = Complexity(normal_search)

ns.set_first_element(data)
