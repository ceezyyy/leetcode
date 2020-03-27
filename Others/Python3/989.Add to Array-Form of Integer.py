"""
@Title: 989. Add to Array-Form of Integer
@Tag: list
@Date: Oct-31 2019
@Author: ceezyyy
@Difficulty: Easy
"""


from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        total = 0
        for i in range(len(A)):
            total = total*10+A[i]
        total += K
        return list(str(total))


'''
Runtime: 440 ms, faster than 15.26% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 14.1 MB, less than 5.00% of Python3 online submissions for Add to Array-Form of Integer.
'''
