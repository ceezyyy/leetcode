"""
@Title: 1002. Find Common Characters
@Tag: str
@Date: Nov-01 2019
@Author: ceezyyy
@Difficulty: Easy
@Reference: https://medium.com/leetcode-cracker/1002-find-common-characters-a80ed5f180ac
"""

from collections import Counter
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counts = Counter(A[0])
        for a in A:
            counts &= Counter(a)  # the intersection of two dicts
        res = []
        for letter, times in counts.items():
            res += letter*times
        return res


def test():
    s = Solution()
    print(s.commonChars(["bella", "label", "roller"]))


if __name__ == "__main__":
    test()


'''
Runtime: 52 ms, faster than 86.99% of Python3 online submissions for Find Common Characters.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Find Common Characters.
'''
