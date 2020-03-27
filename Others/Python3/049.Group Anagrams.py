"""
@Title: 049. Group Anagrams
@Tag: hashtable
@Date: Mar-10 2020
@Author: ceezyyy
@Difficulty: Medium
"""


import collections as c


class Solution:
    def groupAnagrams(self, S: List[str]) -> List[List[str]]:
        d = c.defaultdict(list)
        for s in S:
            d["".join(sorted(s))].append(s)
        return d.values()


"""
Runtime: 104 ms, faster than 54.29% of Python3 online submissions for Group Anagrams.
Memory Usage: 15.9 MB, less than 67.92% of Python3 online submissions for Group Anagrams.
"""


"""
Time Complexity: O(n * nlogn)
Space Complexity: O(n)
"""
