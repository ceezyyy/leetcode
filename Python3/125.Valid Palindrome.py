"""
@Title: 125. Valid Palindrome
@Tag: string
@Date: Jan-14 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch not in set(
            string.punctuation)).replace(" ", "").lower()
        return s == s[::-1]


"""
Runtime: 180 ms, faster than 5.44% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.1 MB, less than 51.19% of Python3 online submissions for Valid Palindrome.
"""
