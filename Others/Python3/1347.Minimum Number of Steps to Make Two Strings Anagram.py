"""
@Title: 1347. Minimum Number of Steps to Make Two Strings Anagram
@Tag: string
@Date: Feb-09 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res, freq = 0, [0] * 26  # lower-case English letters only
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
            if freq[ord(ch) - ord('a')] < 0:
                res += 1
        return res


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
