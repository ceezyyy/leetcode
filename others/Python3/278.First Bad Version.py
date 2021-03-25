"""
@Title: 278. First Bad Version
@Tag: binary search
@Date: Dec-31 2019
@Author: ceezyyy
@Difficulty: Easy
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # corner case
        if n == 1:
            return 1 if isBadVersion(1) == True else 0
        left, right = 1, n
        while left <= right:
            mid = left+(right-left)//2
            if isBadVersion(mid) == False:  # bad version is on the right
                left = mid+1
            else:  # bad version is one the left
                right = mid-1
        return left


"""
Runtime: 24 ms, faster than 91.37% of Python3 online submissions for First Bad Version.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Bad Version.
"""


"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""
