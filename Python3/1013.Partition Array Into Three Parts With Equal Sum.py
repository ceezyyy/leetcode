"""
@Title: 1013. Partition Array Into Three Parts With Equal Sum
@Tag: array
@Date: Feb-05 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # left boundary, right boundary, target sum, total number of elements
        left, right, temp, k, n = 0, 0, 0, sum(A) // 3, len(A)
        for i, a in enumerate(A):  # left part (forward)
            temp += a
            if temp == k:
                left = i  # the position of the left part
                break
        temp = 0  # reset
        for j, a in reversed(list(enumerate(A))):  # right part (backward)
            temp += a
            if temp == k:
                right = j  # the position of the right part
                break
        # "sum(A[left+1:right])" -> the middle part
        return sum(A[left + 1:right]) == k and left < right


"""
Runtime: 320 ms, faster than 97.47% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Memory Usage: 21 MB, less than 6.25% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
