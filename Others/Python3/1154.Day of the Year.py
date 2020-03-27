"""
@Title: 1154. Day of the Year
@Tag: math
@Date: Jan-22 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import calendar


class Solution:
    def dayOfYear(self, date: str) -> int:
        month_days, leap_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [
            31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10])
        return sum(leap_month_days[:month - 1]) + day if calendar.isleap(year) else sum(month_days[:month - 1]) + day


"""
Runtime: 32 ms, faster than 24.55% of Python3 online submissions for Day of the Year.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Day of the Year.
"""
