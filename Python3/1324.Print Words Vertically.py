"""
@Title: 1324. Print Words Vertically
@Tag: string
@Date: Feb-14 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        n = max([len(w) for w in s])
        res = [""] * n
        for i in range(n):
            for word in s:
                res[i] += word[i] if i < len(word) else " "
            res[i] = res[i].rstrip()  # remove trailing spaces
        return res


"""
Runtime: 20 ms, faster than 97.48% of Python3 online submissions for Print Words Vertically.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Print Words Vertically.
"""
