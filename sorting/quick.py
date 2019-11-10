def partition(arr, low, high):
    

def quick(arr, low=None, high=None):
    # ignoring bad input like low w/out high, etc.
    if high is None:
        low, high = 0, len(arr) - 1

    if low < high:
        pivot = partition(arr, low, high)
        quick(arr, low, pivot - 1) 
        quick(arr, pivot + 1, high)

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
    # nums = [random.randint(0, 1000) for x in range(100)]
    # test(sorted(nums), nums)
    # nums = [random.randint(0, 1000) for x in range(1000)]
    # test(sorted(nums), nums)
    # nums = [random.randint(0, 1000) for x in range(10000)]
    # test(sorted(nums), nums)
