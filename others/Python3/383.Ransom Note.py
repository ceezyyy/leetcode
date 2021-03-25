"""
@Title: 383. Ransom Note
@Tag: array / hashtable
@Date: Feb-28 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Approach 1: (Hashtable)


import collections as c


class Solution:
    def canConstruct(self, R: str, M: str) -> bool:
        d = c.defaultdict(int)
        for r in R:
            d[r] -= 1  # mark it as negative
        for m in M:
            if m in d:  # showed up before
                d[m] += 1
        for v in d.items():
            if v[1] < 0:
                return False
        return True


# Approach 2: (Array)


class Solution:
    def canConstruct(self, R: str, M: str) -> bool:
        d = [0] * 26  # only 26 lowercase letters
        for r in R:
            d[ord(r)-ord('a')] -= 1
        for m in M:
            if d[ord(m)-ord('a')] < 0:  # appeared before
                d[ord(m)-ord('a')] += 1
        for a in d:
            if a < 0:
                return False
        return True


"""
Runtime: 64 ms, faster than 44.94% of Python3 online submissions for Ransom Note.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Ransom Note.
"""
