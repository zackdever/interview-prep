# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        strike = prices[0]
        sell = prices[0]
        profit = 0
        for p in prices:
            if p < strike:
                strike = p
                sell = p
            elif p > sell:
                sell = p
            if sell - strike > profit:
                profit = sell - strike
        return profit

    # def maxProfit(self, prices: List[int]) -> int:
        # build an index of days per price. sort prices.
        # keep checking biggest delta, and if the days are in the right order
        # return, otherwise check the next biggest delta
        # from collections import defaultdict
        # days = defaultdict
        # for i, p in enumerate(prices):
            # days[p].append(i)

        # prices = sorted(prices)
        # for i in prices:

    """brute force (time exceeded)"""
    # def max_for_strike(self, strike, prices):
        # return max([0, max(prices) - strike])

    # def maxProfit(self, prices: List[int]) -> int:
        # cheapest = 0
        # big = 0
        # for i in range(len(prices[:-1])):
            # profit = self.max_for_strike(prices[i], prices[i + 1:])
            # if profit > big:
                # big = profit
        # return big

def test(expected, *args):
    result = Solution().maxProfit(*args)
    if result == expected:
        print("passed")
    else:
        print("expected {}, but got {}".format(expected, result))

if __name__ == '__main__':
    test(0, [])
    test(0, [1])
    test(5, [7,1,5,3,6,4])
    test(0, [7,6,4,3,1])
    test(8, [2,4,3,10,1,5,8])
