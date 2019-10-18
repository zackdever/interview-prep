from typing import List

def pivotIndex(nums: List[int]) -> int:
    # this works, but the real answer is get the total sum once,
    # and then build up the left sum as you go and substract it
    # and the current index value to see if they match
        left = 0
        right = sum(nums[1:])
        for i in range(len(nums) - 1):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i+1]
        if left == right:
            return len(nums) - 1
        return -1
            

        # brute force too slow
        # for i in range(len(nums)):
            # if sum(nums[:i]) == sum(nums[i+1:]):
                # return i
        # return -1

    # left = nums[0]
    # right = sum(nums[2:])
    # for i in range(len(nums[2:-1])):
        # if left == right:
            # return i+1
        # left += nums[i+1]
        # right -= nums[i+2]
    # return -1

if __name__ == '__main__':
    print(pivotIndex([1,7,3,6,5,6]))
    print(pivotIndex([-1,-1,-1,-1,1,0]))
    print(pivotIndex([-1,-1,0,1,1,0]))
    print(pivotIndex([-1,-1,-1,1,1,1]))

