"""
@Title: 345. Reverse Vowels of a String
@Tag: str
@Date: Jan-26 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right, vowels, s = 0, len(s) - 1, list("aeiouAEIOU"), list(s)
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]  # swap
                left += 1  # forward
                right -= 1  # backward
            if s[left] not in vowels:
                left += 1  # forward
            if s[right] not in vowels:
                right -= 1  # backward
        return "".join(s)


"""
Runtime: 68 ms, faster than 33.72% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Reverse Vowels of a String.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
