"""
@Title: 374. Guess Number Higher or Lower
@Tag: binary search
@Date: Dec-27 2019
@Author: ceezyyy
@Difficulty: Easy
"""


# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n  # left bound, right bound
        while(left <= right):
            mid = (left+right)//2
            if guess(mid) == 0:  # Congrats! You got it!
                return mid
            else:  # not found
                if guess(mid) == 1:  # my number is higher
                    left = mid+1
                else:  # my number is lower
                    right = mid-1


"""
Runtime: 24 ms, faster than 82.65% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower.
"""
