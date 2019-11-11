def sequential(v, arr):
    """O(n) returns first index of v, or -1 if not present."""
    for i, x in enumerate(arr):
        if v == x:
            return i
    return -1

def binary(v, arr, start=None, end=None):
    """Assumes arr is sorted.
    O(log(n)) returns first index of v, or -1 if not present.
    """
    if end is None:
        start = 0
        end = len(arr) - 1
        # optimization
        if v < arr[start] or v > arr[end]:
            return -1

    # instead of recursion, could use a while loop and update start/end
    if start <= end:
        p = (start + end) // 2  
        if v == arr[p]:
            return p
        elif v > arr[p]:
            return binary(v, arr, p + 1, end)
        else:
            return binary(v, arr, start, p - 1)

    return -1

if __name__ == '__main__':
    assert(sequential(42, [7, 3, 2, 42, 8, 1]) == 3)
    assert(sequential(44, [7, 3, 2, 42, 8, 1]) == -1)
    assert(binary(42, [1, 2, 3, 7, 8, 42]) == 5)
    assert(binary(3, [1, 2, 3, 7, 8, 42]) == 2)
    assert(binary(44, [1, 2, 3, 7, 8, 42]) == -1)
    assert(binary(6, [1, 2, 3, 7, 8, 42]) == -1)
