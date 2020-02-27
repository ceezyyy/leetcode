"""
@Title: 599. Minimum Index Sum of Two Lists
@Tag: hashtable
@Date: Feb-27 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def findRestaurant(self, A: List[str], B: List[str]) -> List[str]:
        d, res = {}, []
        for i, a in enumerate(A):  # no duplicates in both lists
            d[a] = i + 1  # avoid the case of "0"
        for i, b in enumerate(B):
            if b in d:  # common interest
                d[b] = -d[b] - i  # mark it as negative
        smallest = -min([abs(x)
                         for x in d.values() if x < 0])  # minimum index sum
        for v in d.items():  # restaurant: index sum
            if v[1] == smallest:
                res.append(v[0])
        return res


"""
Runtime: 156 ms, faster than 72.45% of Python3 online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Minimum Index Sum of Two Lists.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
