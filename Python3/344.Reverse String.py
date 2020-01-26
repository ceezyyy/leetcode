"""
@Title: 344. Reverse String
@Tag: str
@Date: Jan-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Solution one:

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]  # in-place


"""
Runtime: 204 ms, faster than 93.45% of Python3 online submissions for Reverse String.
Memory Usage: 17.3 MB, less than 95.35% of Python3 online submissions for Reverse String.
"""


# Solution 2: Two pointers

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


"""
Runtime: 248 ms, faster than 9.41% of Python3 online submissions for Reverse String.
Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Reverse String.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
