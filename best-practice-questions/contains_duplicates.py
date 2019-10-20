# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """you could brute force this with an inner loop as well..."""
        lookup = set()
        for n in nums:
            if n in lookup:
                return True
            lookup.add(n)
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        """sort!"""
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False


def test(expected, *args):
    result = Solution().containsDuplicate(*args)
    if result == expected:
        print("passed")
    else:
        print("expected {}, but got {}".format(expected, result))

if __name__ == '__main__':
    test(True, [1,2,3,1])
    test(False, [1,2,3,4])
    test(True, [1,1,1,3,3,4,3,2,4,2])
