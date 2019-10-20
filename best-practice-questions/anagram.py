# https://leetcode.com/problems/valid-anagram/

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # obvious solution
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        from collections import defaultdict
        counter = defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
            counter[t[i]] -= 1

        return all(c == 0 for c in counter.values())


def test(expected, *args):
    result = Solution().isAnagram(*args)
    if result == expected:
        print("passed")
    else:
        print("expected {}, but got {}".format(expected, result))

if __name__ == '__main__':
    test(True, "anagram", "nagaram")
    test(False, "rat", "car")
