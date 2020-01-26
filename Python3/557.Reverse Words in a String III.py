"""
@Title: 557. Reverse Words in a String III
@Tag: str
@Date: Jan-26 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split())


"""
Runtime: 80 ms, faster than 14.46% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 13.1 MB, less than 96.15% of Python3 online submissions for Reverse Words in a String III.
"""
