# TODO practice typing these in a google doc

def bubble(arr):
    # O(n^2)
    # bubbles up larger elements to the right, forming a sorted right partition
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion(arr):
    # O(n^2)
    # sort of like sorting a deck of cards. starting from the left, if you find
    # a smaller item, keep swapping it back until it's in order
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection(arr):
    # O(n^2)
    # starting from the left, find the smallest element in the unsorted right
    # partition. if it's smaller, swap it. repeat. this builds a sorted left array
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def mergesort(arr):
    # O(n*log(n))
    # recursively split array into halves until each is 0 or 1 element
    # (by definition these are sorted), and then merge the sorted arrays together
    n = len(arr)
    if n < 2:
        return arr

    half = n // 2
    merged = [0] *  n # or [] and use .append instead of i
    # merged = []
    left = mergesort(arr[:half])
    right = mergesort(arr[half:])
    l, r, i = 0, 0, 0
    # l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged[i] = left[l]
            # merged.append(left[l])
            l += 1
        else:
            merged[i] = right[r]
            # merged.append(right[r])
            r += 1
        i += 1

    for x in left[l:]:
        merged[i] = x
        i += 1

    for x in right[r:]:
        merged[i] = x
        i += 1
    # merged.extend(left[l:])
    # merged.extend(right[r:])

    return merged

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


if __name__ == '__main__':
    test()
