"""
@Title: 859. Buddy Strings
@Tag: string
@Date: Feb-25 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            if len(A) == len(set(A)):  # "abcdefg"
                return False
            else:  # "aaaa"
                return True
        n = len(A)
        res = [(x, y) for x, y in zip(A, B) if x != y]  # pairs
        return len(res) == 2 and res[0] == res[1][::-1]


"""
Runtime: 32 ms, faster than 61.54% of Python3 online submissions for Buddy Strings.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Buddy Strings.
"""
