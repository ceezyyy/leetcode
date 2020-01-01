"""
@Title: 1304. Find N Unique Integers Sum up to Zero
@Tag: array
@Date: Jan-01 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 != 0:  # n is odd
            res.append(0)
            for i in range(1, (n//2)+1):
                res.append(i)
                res.append(-i)
        else:  # n is even
            for j in range(1, (n//2)+1):
                res.append(j)
                res.append(-j)
        return res


"""
Runtime: 32 ms, faster than 58.15% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
