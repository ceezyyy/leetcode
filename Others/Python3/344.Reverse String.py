"""
@Title: 344. Reverse String
@Tag: str
@Date: Jan-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Solution 1:

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


# Solution 3: Recursion

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursive(left, right):
            if left >= right:  # exit
                return s
            s[left], s[right] = s[right], s[left]  # swap
            recursive(left + 1, right - 1)
        return recursive(0, len(s) - 1)


"""
Runtime: 224 ms, faster than 26.55% of Python3 online submissions for Reverse String.
Memory Usage: 42.9 MB, less than 5.81% of Python3 online submissions for Reverse String.
"""
