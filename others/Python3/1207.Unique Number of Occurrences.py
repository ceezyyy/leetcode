"""
@Title: 1207. Unique Number of Occurrences
@Tag: dict
@Date: Nov-11 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = []
        d = {item: {'occurrence': 0} for item in arr}  # dict
        for c in arr:
            d[c]['occurrence'] += 1
        for c in d:
            res.append(d[c]['occurrence'])
        return len(set(res)) == len(res)


"""
Runtime: 36 ms, faster than 95.70% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.
"""
