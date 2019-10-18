from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        di = -1
        largest = 0
        stillbig = 0
        for i, num in enumerate(nums):
            if num > largest:
                di = i
                stillbig = largest
                largest = num
            elif num > stillbig:
                stillbig = num
        if largest >= stillbig * 2:
            return di
        return -1


if __name__ == '__main__':
    print(Solution().dominantIndex([0,0,3,2]))
    print(Solution().dominantIndex([3, 6, 1, 0]))
    print(Solution().dominantIndex([3, 6, 1, 0]) == 1)
    print(Solution().dominantIndex([1, 2, 3, 4]) == -1)
