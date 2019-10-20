from typing import List

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        # """Brute force"""
        # for i, n in enumerate(nums):
            # for i2, n2 in enumerate(nums[i+1:]):
                # if n + n2 == target:
                    # return [i, i2+i+1]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hash table"""
        from collections import defaultdict
        value_position = defaultdict(list)
        for i, n in enumerate(nums):
            complement = target - n
            if value_position[complement]:
                return [value_position[complement][0], i]
            value_position[n].append(i)


def test(expected, *args):
    result = Solution().twoSum(*args)
    if result == expected:
        print("passed")
    else:
        print("expected {}, but got {}".format(expected, result))

if __name__ == '__main__':
    test([0, 1], [2, 7, 11, 15], 9)
    test([1, 3], [2, 7, 11, 15], 22)
    test([1, 2], [2, 7, 7, 7], 14)
