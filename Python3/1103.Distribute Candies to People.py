"""
@Title: 1103. Distribute Candies to People
@Tag: array
@Date: Feb-25 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def distributeCandies(self, c: int, n: int) -> List[int]:
        res = [0] * n
        i, per = 0, 1
        while c > 0:
            if i == n:
                i = 0
            res[i], c, per = res[i] + per, c - per, per + 1
            per = c if c < per + 1 else per
            i += 1
        return res


"""
Runtime: 36 ms, faster than 66.20% of Python3 online submissions for Distribute Candies to People.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Distribute Candies to People.
"""
