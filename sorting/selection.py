def selection(nums):
    n = len(nums)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # could do a check to see if min_idx != i
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

def test(expected, *args):
    result = selection(*args)
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
