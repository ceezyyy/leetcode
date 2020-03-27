"""
@Title: 151. Reverse Words in a String
@Tag: string
@Date: Feb-29 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


"""
Runtime: 24 ms, faster than 90.00% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Reverse Words in a String.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
