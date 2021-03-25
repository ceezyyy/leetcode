"""
@Title: 1266. Minimum Time Visiting All Points
@Tag: math
@Date: Jan-23 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res, hor, ver = 0, [h[0] for h in points], [v[1]
                                                    for v in points]  # horizontal & vertical
        for k in range(len(hor) - 1):
            # kinda like Manhattan distance
            res += max(abs(hor[k+1] - hor[k]), abs(ver[k+1] - ver[k]))
        return res


"""
Runtime: 76 ms, faster than 11.34% of Python3 online submissions for Minimum Time Visiting All Points.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.
"""
