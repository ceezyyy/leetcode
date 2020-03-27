"""
@Title: 849. Maximize Distance to Closest Person
@Tag: array / pointer
@Date: Feb-02 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last, res = -1, 0  # "last" -> the last appearance(index) of "1"
        for i in range(len(seats)):  # one pass
            if seats[i] == 1:
                if last == -1:  # "pre" (e.g: [0, 0, 0, 1])
                    res = max(res, i)  # "i" -> the first appearance of "1"
                else:
                    res = max(res, (i - last) // 2)  # "middle"
                last = i  # update the pointer
        # "post" (e.g: [1, 0, 0, 0])
        return max(res, len(seats) - 1 - last) if last != len(seats) - 1 else res


"""
Runtime: 132 ms, faster than 91.28% of Python3 online submissions for Maximize Distance to Closest Person.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Maximize Distance to Closest Person.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
