"""
@Title: 1360. Number of Days Between Two Dates
@Tag: 
@Date: Feb-23 2020
@Author: ceezyyy
@Difficulty: Easy
"""


from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_format = "%Y-%m-%d"
        a = datetime.strptime(date1, date_format)
        b = datetime.strptime(date2, date_format)
        return abs((b - a).days)


"""
Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Number of Days Between Two Dates.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Number of Days Between Two Dates.
"""
