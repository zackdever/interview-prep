def merge(left, right):
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    # append any remaining elements from left or right
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged

def mergesort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    partition = n // 2
    return merge(mergesort(nums[:partition]), mergesort(nums[partition:]))

def test(expected, *args):
    result = mergesort(*args)
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
    nums = [random.randint(0, 1000) for x in range(10000)]
    test(sorted(nums), nums)
