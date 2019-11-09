def bubble(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j+1]:
                swapped = True
                swap = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = swap
        if not swapped:
            break
    return nums

def test(expected, *args):
    result = bubble(*args)
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
