"""
@Title: 1306. Jump Game III
@Tag: recursion
@Date: Feb-14 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def canReach(self, A: List[int], i: int) -> bool:
        if (0 <= i < len(A)) and A[i] >= 0:
            if A[i] == 0:
                return True
            A[i] = -A[i]  # have seen before
            # either
            return self.canReach(A, i + A[i]) or self.canReach(A, i - A[i])
        return False


"""
Runtime: 248 ms, faster than 45.58% of Python3 online submissions for Jump Game III.
Memory Usage: 19.2 MB, less than 100.00% of Python3 online submissions for Jump Game III.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
