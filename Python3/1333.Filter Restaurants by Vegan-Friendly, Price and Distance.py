"""
@Title: 1333. Filter Restaurants by Vegan-Friendly, Price and Distance
@Tag: array
@Date: Feb-12 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def filterRestaurants(self, R: List[List[int]], v: int, p: int, d: int) -> List[int]:
        # filter restaurant
        if v == 0:  # any restaurant
            rest = [r[0] for r in R]
        else:
            rest = [r[0] for r in R if r[2] == 1]
        for r in R:  # filter price & distance
            if (r[3] > p or r[4] > d) and r[0] in rest:
                rest.remove(r[0])
        return [res[1] for res in reversed(sorted([r[1], r[0]] for r in R if r[0] in rest))]


"""
Runtime: 1120 ms, faster than 5.13% of Python3 online submissions for Filter Restaurants by Vegan-Friendly, Price and Distance.
Memory Usage: 21.4 MB, less than 100.00% of Python3 online submissions for Filter Restaurants by Vegan-Friendly, Price and Distance.
"""
