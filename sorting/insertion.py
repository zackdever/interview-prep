# def insertion(nums):
    # """this is what i came up with aftering watching an insertion sort"""
    # for i in range(len(nums)):
        # for j in range(i):
            # if nums[i-j] < nums[i-j-1]:
                # nums[i-j], nums[i-j-1] = nums[i-j-1], nums[i-j]
            # else:
                # break
    # return nums

def insertion(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

def test(expected, *args):
    result = insertion(*args)
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
