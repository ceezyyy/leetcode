"""
@Title: 041. First Missing Positive
@Tag: array / hashmap
@Date: Feb-26 2020
@Author: ceezyyy
@Difficulty: Hard
"""


# Approach 1: (Hashmap)


import collections as c


class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        biggest, d = float("-inf"), c.defaultdict(int)
        for a in A:
            # update the biggest positive so far
            biggest = a if a > 0 and a > biggest else biggest
            d[a] += 1  # value: freq
        if biggest == float("-inf"):  # all the elements is negative or zero
            return 1
        for i in range(1, biggest):
            if d[i] == 0:
                return i
        return biggest + 1


"""
Runtime: 32 ms, faster than 78.28% of Python3 online submissions for First Missing Positive.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for First Missing Positive.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
