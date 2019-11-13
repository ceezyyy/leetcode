"""
@Title: 451. Sort Characters By Frequency
@Tag: Counter
@Date: Nov-13 2019
@Author: ceezyyy
@Difficulty: Medium
"""


import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c*times for c, times in collections.Counter(s).most_common())

# Counter.most_common(n: int) -> List[Tuple[_T, int]]
# List the n most common elements and their counts from the most common to the least. If n is None, then list all element counts.
# >>> Counter('abcdeabcdabcaba').most_common(3)
# [('a', 5), ('b', 4), ('c', 3)]


def test():
    s = Solution()
    res = s.frequencySort(
        "ajsfhjksdfgjkdfjkdfjgdsdgfffffsdofiasdofffffffffffdsaddrrrrrrrrrrrrr")
    print(res)


if __name__ == "__main__":
    test()
