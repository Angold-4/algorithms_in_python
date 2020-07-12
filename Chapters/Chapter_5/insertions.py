# Angold4 20200712
def insertion_sort(A):
    """sort list of comparable elements into nondecreasing order"""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur


if __name__ == "__main__":
    A = [3, 2, 9, 1, 4, 10, -1, 213]
    insertion_sort(A)
    print(A)   # [-1, 1, 2, 3, 4, 9, 10, 213]
    """
    If the list is decreasing. The Complexity is O(n^2)
    Beacause the number of iterations is arithmetic sequence
    """
