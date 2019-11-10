def bubble(nums):
    # O(n^2)
    # bubble up bigger terms to the right
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

def insertion(nums):
    # O(n^2)
    # kind of like sorting deck of cards. start from the left, and when
    # you find a smaller item, keep inserting it back until it's in order
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

def selection(nums):
    # O(n^2)
    # starting from left, find the smallest element and if it's smaller than
    # the item on the left, swap them
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums

def mergesort(nums):
    # O(n log(n))
    # recursively split into subarrays until each subarray is just
    # one element (sorted) and then merge the sorted arrays back together
    n = len(nums)
    if n < 2:
        return nums

    split_idx = n // 2
    left = mergesort(nums[:split_idx])
    right = mergesort(nums[split_idx:])

    # merge
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged.extend(left[l:])
    merged.extend(right[r:])
    
    return merged

def test():
    import random

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = bubble(nums)
    expected = sorted(nums)
    if result == expected:
        print("bubble passed")
    else:
        print("bubble expected {}, but got {}".format(expected, result))

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = insertion(nums)
    expected = sorted(nums)
    if result == expected:
        print("insertion passed")
    else:
        print("insertion expected {}, but got {}".format(expected, result))

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = selection(nums)
    expected = sorted(nums)
    if result == expected:
        print("selection passed")
    else:
        print("selection expected {}, but got {}".format(expected, result))

    nums = [random.randint(0, 1000) for x in range(1000)]
    result = mergesort(nums)
    expected = sorted(nums)
    if result == expected:
        print("mergesort passed")
    else:
        print("mergesort expected {}, but got {}".format(expected, result))


if __name__ == '__main__':
    test()
