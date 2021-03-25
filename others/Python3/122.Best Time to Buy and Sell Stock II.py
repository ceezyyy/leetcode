"""
@Title: 122. Best Time to Buy and Sell Stock II
@Tag: 
@Date: Dec-18 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # no corner case
        for i in range(len(prices)-1):  # for loop
            # benefit of each transaction in order to get the maximum profit
            if prices[i+1]-prices[i] > 0:  # benefit
                profit += prices[i+1]-prices[i]  # accumulation
        return profit


"""
Runtime: 60 ms, faster than 91.03% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 13.8 MB, less than 87.81% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""
