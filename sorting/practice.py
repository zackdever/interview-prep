# TODO practice typing these in a google doc

def bubble(arr):
    # O(n^2) bubbles larger elements up.
    # can optimize for mostly sorted lists by breaking when we're sorted
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr

def insertion(arr):
    # O(n^2) like sorting a deck of cards.
    # start from left and look at each item. if it's smaller than the item
    # behind it, keep going back until you find where it belongs
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection(arr):
    # O(n^2) start from the left and look at the entire array.
    # find the smallest element and move to the left. move index to the
    # right and repeat
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

def mergesort(arr):
    # O(n*log(n))
    # recursively split into subarrays until they are 0 or 1 in length.
    # these are now all sorted individually. merge them together, sorting
    # when merging
    n = len(arr)

    # base case
    if n < 2:
        return arr

    # recursively split
    middle = n // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])

    # merge
    l, r = 0, 0
    merged = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    # add any remaining items
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged

def _quick_partition(arr, low, high):
    pivot = arr[high]
    left = low
    right = high - 1

    while left <= right:
        if arr[left] > pivot and arr[right] <= pivot:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] <= pivot:
            left += 1
        if arr[right] > pivot:
            right -= 1

    # remember to swap the pivot to the correct position
    arr[left], arr[high] = arr[high], arr[left]

    return left


def quick(arr, low=None, high=None):
    """
    Best/avg time: O(n*log(n))
    worst: O(n^2)
    worst can mostly be avoided by picking a good pivot
    in place. pick a pivot, swap in place all elements less than pivot to the left,
    all elements greater than pivot to the right. the pivot is now sorted.
    recursively quick sort left and right subarrays in place.
    """
    if high is None:
        low, high = 0, len(arr) - 1

    if low < high:
        p_idx = _quick_partition(arr, low, high)
        quick(arr, low, p_idx - 1)
        quick(arr, p_idx + 1, high)

    return arr

    
def test():
    import random

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = bubble(nums)
    expected = sorted(nums)
    if result == expected:
        print("bubble passed")
    else:
        print("bubble failed!")
        # print("bubble expected {}, but got {}".format(expected, result))

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = insertion(nums)
    expected = sorted(nums)
    if result == expected:
        print("insertion passed")
    else:
        print("insertion failed!")
        # print("insertion expected {}, but got {}".format(expected, result))

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = selection(nums)
    expected = sorted(nums)
    if result == expected:
        print("selection passed")
    else:
        print("selection failed!")
        # print("selection expected {}, but got {}".format(expected, result))

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = mergesort(nums)
    expected = sorted(nums)
    if result == expected:
        print("mergesort passed")
    else:
        print("mergesort failed!")
        # print("mergesort expected {}, but got {}".format(expected, result))

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = quick(nums)
    expected = sorted(nums)
    if result == expected:
        print("quick passed")
    else:
        print("quick failed!")
        # print("quick expected {}, but got {}".format(expected, result))


if __name__ == '__main__':
    test()
