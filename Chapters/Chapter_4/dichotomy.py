#  Position elements in an ordered array(Normal Way) Angold4 20200611
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
