"""
@Title: 121. Best Time to Buy and Sell Stock
@Tag: stack
@Date: Dec-17 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # corner case
        if not prices:
            return 0
        stack = [prices[0]]  # initialization
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < stack[-1]:  # always the min element
                stack.pop()
                stack.append(prices[i])
            # find the maximum profit
            profit = max(prices[i]-stack[-1], profit)
        return profit


"""
Runtime: 68 ms, faster than 71.83% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 98.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
