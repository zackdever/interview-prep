from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # simple solution
        # num = int(''.join(map(str, digits))) + 1
        # return list(map(int, str(num)))

        # faster
        limit = len(digits) - 1
        for i, d in enumerate(reversed(digits)):
            if d < 9:
                digits[limit - i] += 1
                break
            else:
                digits[limit - i] = 0
            if i == limit:
                digits.insert(0, 1)
        return digits

    

def test(args, expected):
    result = Solution().plusOne(args)
    if result == expected:
        print("passed")
    else:
        print("expected {}, but got {}".format(expected, result))

if __name__ == '__main__':
    test([1,2,3], [1,2,4])
    test([4,3,2,1], [4,3,2,2])
    test([0], [1])
    test([1,2,9], [1,3,0])
    test([1,9,9], [2,0,0])
    test([9,9,9], [1,0,0,0])
