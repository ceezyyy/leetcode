"""
@Title: 455. Assign Cookies
@Tag: greedy
@Date: Dec-23 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # greedy
        res = 0  # the number of your content children, which we want to maximize
        g.sort()  # in increasing order
        s.sort()  # in increasing order
        index = 0  # the last location of the size that will content children, initialize as zero
        for i in range(len(g)):
            for j in range(index, len(s)):
                if s[j] >= g[i]:  # the children will be content
                    res += 1
                    index = j+1  # update the location
                    break  # jump to the next child
        return res


"""
Runtime: 180 ms, faster than 64.03% of Python3 online submissions for Assign Cookies.
Memory Usage: 14.4 MB, less than 85.71% of Python3 online submissions for Assign Cookies.
"""
