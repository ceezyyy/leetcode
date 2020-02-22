"""
@Title: 056. Merge Intervals
@Tag: array / sort
@Date: Feb-22 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def merge(self, I: List[List[int]]) -> List[List[int]]:
        res, I = [], sorted(I)
        if not I:  # corner case
            return None
        for i in I:
            if not res or i[0] > res[-1][1]:  # new event
                res.append(i)
            else:  # overlapping
                res[-1][1] = max(i[1], res[-1][1])  # update the finish time
        return res


"""
Runtime: 88 ms, faster than 67.59% of Python3 online submissions for Merge Intervals.
Memory Usage: 14.6 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
