"""
@Title: 1013. Partition Array Into Three Parts With Equal Sum
@Tag: array
@Date: Feb-05 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        temp, k, n = 0, sum(A) // 3, len(A)  # "k" -> target sum
        for i, a in enumerate(A):  # left part (forward)
            temp += a
            if temp == k:
                left = i  # the position of the left part
                break
        temp = 0  # reset
        for j in range(n - 1, -1, -1):  # right part (backward)
            temp += A[j]
            if temp == k:
                right = j  # the position of the right part
                break
        # "sum(A[left + 1:right])" -> the middle part
        return sum(A[left + 1:right]) == k and left < right


"""
Runtime: 336 ms, faster than 72.96% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
Memory Usage: 19.3 MB, less than 6.25% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
