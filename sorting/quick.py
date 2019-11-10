def partition(arr, low, high):
    pivot = arr[high]
    left = low
    right = high - 1
    
    while left <= right:
        if arr[left] > pivot and arr[right] <= pivot:
            arr[left], arr[right] = arr[right], arr[left]
        elif arr[left] <= pivot:
            left += 1
        elif arr[right] > pivot:
            right -= 1

    arr[left], arr[high] = arr[high], arr[left]
    return left
    

def quick(arr, low=None, high=None):
    """
    O(n*log(n)). In place!
    Pick a pivot, and swap all elements lte  the pivot to the left.
    All elements greater than pivot are swapped to the right. Recurisvely quicksort
    left and right subarrays.
    """
    # ignoring bad input like low w/out high, etc.
    if high is None:
        low, high = 0, len(arr) - 1

    if low < high:
        p_idx = partition(arr, low, high)
        quick(arr, low, p_idx - 1) 
        quick(arr, p_idx + 1, high)

    return arr

def test(expected, *args):
    result = quick(*args)
    if result == expected:
        print("passed")
    else:
        print("expected {}, but got {}".format(expected, result))

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for x in range(10)]
    test(sorted(nums), nums)
    nums = [random.randint(0, 1000) for x in range(100)]
    test(sorted(nums), nums)
    nums = [random.randint(0, 1000) for x in range(1000)]
    test(sorted(nums), nums)
    nums = [random.randint(0, 1000) for x in range(100000)]
    test(sorted(nums), nums)
