"""
@Title: 5315. Maximum 69 Number
@Tag: string
@Date: Jan-19 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        # str.replace(old, new[,a max])
        return int(str(num).replace('6', '9', 1))


"""
Runtime: 28 ms, faster than 66.67% of Python3 online submissions for Maximum 69 Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Maximum 69 Number.
"""
