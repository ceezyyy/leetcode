"""
@Title: 003. Longest Substring Without Repeating Characters
@Tag: sliding window
@Date: Feb-25 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Approach 1: Brute Force


class Solution:
    def lengthOfLongestSubstring(self, A: str) -> int:
        n, res = len(A), -1
        for i in range(n):
            seen = set(A[i])
            temp = 0
            for j in range(i+1, n):
                if A[j] in seen:  # repeated
                    break
                else:
                    seen.add(A[j])
                    temp += 1
            res = max(res, temp + 1)
        return res if res != -1 else 0


"""
Runtime: 584 ms, faster than 12.87% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13 MB, less than 99.49% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
