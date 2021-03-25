"""
@Title: 1344. Angle Between Hands of a Clock
@Tag: math
@Date: Feb-10 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def angleClock(self, h: int, m: int) -> float:
        # "m / 60 * 5" means how the minute hand affects the position of the hour hand
        h = 0 + m / 60 * 5 if h == 12 else h * 5 + m / 60 * 5  # convert hrs to mins
        return min(abs(m - h) * 6, 360 - abs(m - h) * 6)  # the smaller one


"""
Runtime: 32 ms, faster than 22.88% of Python3 online submissions for Angle Between Hands of a Clock.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Angle Between Hands of a Clock.
"""
