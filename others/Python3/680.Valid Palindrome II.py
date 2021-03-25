"""
@Title: 680. Valid Palindrome II
@Tag: string
@Date: Jan-27 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # either (you may delete at most one character)
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            else:
                left, right = left + 1, right - 1  # move pointers
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1  # move pointers
        return True


"""
Runtime: 180 ms, faster than 35.55% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 13.2 MB, less than 75.00% of Python3 online submissions for Valid Palindrome II.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
