"""
@Title: 1328. Break a Palindrome
@Tag: string
@Date: Feb-12 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p) == 1:  # corner case
            return ""
        p = list(p)  # convert to list in order to modify
        for i, ch in enumerate(p):
            if ch != 'a' and i != len(p) // 2:  # e.g: "aba"
                p[i] = 'a'  # modify
                break
            if i == len(p) - 1:  # the last element
                p[i] = 'b'  # e.g: "aaa"
        return "".join(p)


"""
Runtime: 24 ms, faster than 90.00% of Python3 online submissions for Break a Palindrome.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Break a Palindrome.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
