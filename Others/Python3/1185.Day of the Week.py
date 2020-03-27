"""
@Title: 1185. Day of the Week
@Tag: 
@Date: Feb-06 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime("%A")


"""
Runtime: 24 ms, faster than 85.23% of Python3 online submissions for Day of the Week.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Day of the Week.
"""
