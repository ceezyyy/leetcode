"""
@Title: 125. Valid Palindrome
@Tag: string
@Date: Jan-14 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Solution one:


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch not in set(
            string.punctuation)).replace(" ", "").lower()
        return s == s[::-1]


"""
Runtime: 180 ms, faster than 5.44% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.1 MB, less than 51.19% of Python3 online submissions for Valid Palindrome.
"""


# Solution two: Two pointers


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1  # two pointers
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():  # ignoring cases
                    return False
                else:
                    left += 1
                    right -= 1
            elif not s[left].isalnum():  # left is not a alphanumeric
                left += 1
            else:  # right is not a alphanumeric
                right -= 1
        return True


"""
Runtime: 68 ms, faster than 13.98% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.3 MB, less than 76.19% of Python3 online submissions for Valid Palindrome.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
