"""
@Title: 290. Word Pattern
@Tag: hashtable
@Date: Feb-27 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def wordPattern(self, P: str, S: str) -> bool:
        S, d1, d2 = S.split(), {}, {}
        if len(P) != len(S):
            return False
        for p, s in zip(P, S):  # bijection (one to one)
            if p not in d1 and s not in d2:  # both not in
                d1[p], d2[s] = s, p
            elif p in d1 and s in d2:  # both in
                if (d1[p], d2[s]) != (s, p):
                    return False
            else:  # not a bijection
                return False
        return True


"""
Runtime: 24 ms, faster than 86.40% of Python3 online submissions for Word Pattern.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Word Pattern.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
