from typing import List

# welp this is tough! i think i'll go throught the lessons
# and solve the ones i feel like, but mostly focus on the lessons.
# then i'll just work on problems, working my way up

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # do i need to protect against empties?
        rowcount = len(matrix)
        colcount = len(matrix[0])
        row = 0
        col = 0
        diag = []
        while row < rowcount - 1:
            while col < colcount -1:
                if row
    

def test(args, expected):
    result = Solution().findDiagonalOrder(args)
    if result == expected:
        print("passed")
    else:
        print("expected {}, but got {}".format(expected, result))

if __name__ == '__main__':
    test([
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
            ],
            [1,2,4,7,5,3,6,8,9])
