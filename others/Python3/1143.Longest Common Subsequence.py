"""
@Title: 1143. Longest Common Subsequence
@Tag: dp
@Date: Dec-22 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # LCS
        m, n = len(text1)+1, len(text2)+1
        # initialization (already to make the first row and col to be zero)
        dp = [[0 for i in range(n)] for j in range(m)]  # memory
        # m * n matrix
        for i in range(1, m):  # for loop
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:  # if match
                    dp[i][j] = 1+dp[i-1][j-1]
                else:  # not match
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[i][j]


"""
Runtime: 456 ms, faster than 41.11% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 21.4 MB, less than 100.00% of Python3 online submissions for Longest Common Subsequence.
"""


"""
Longest Common Subsequence (2 Strings) - Dynamic Programming & Competing Subproblems - YouTube
https://www.youtube.com/watch?v=ASoaQq66foQ
"""
