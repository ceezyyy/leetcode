"""
@Title: 746. Min Cost Climbing Stairs
@Tag: DP
@Date: Nov-17 2019
@Author: ceezyyy
@Difficulty: Easy
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Memory recursion
        # min cost to n-th step(exclude the cost of n-th step)
        dp = [0]*(len(cost)+1)
        for n in range(2, len(cost)+1):
            dp[n] = min(dp[n-1]+cost[n-1], dp[n-2]+cost[n-2])
        return dp[n]


def test():
    s = Solution()
    res = s.minCostClimbingStairs(
        [10, 15, 1, 20, 100, 30, 100, 1, 2, 30, 60, 100])
    print(res)  # 124


if __name__ == "__main__":
    test()


"""
Runtime: 56 ms, faster than 96.49% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Min Cost Climbing Stairs.
"""
