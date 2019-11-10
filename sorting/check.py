def bubble(arr):
    return []

def insertion(arr):
    return []

def selection(arr):
    return []

def mergesort(arr):
    return []

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
