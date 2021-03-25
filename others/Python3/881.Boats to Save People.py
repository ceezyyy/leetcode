"""
@Title: 881. Boats to Save People
@Tag: two pointers
@Date: Jan-25 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)  # from lightest to heaviest
        i, j, res = 0, len(people) - 1, 0  # i -> lightest, j -> heaviest
        while i <= j:
            # here "i == j" represent there are only one person to carry
            if people[j] == limit or i == j:  # case 1: only one person
                res += 1
                j -= 1  # move the pointer
            else:  # case 2: try to carry two people together
                if people[i] + people[j] <= limit:  # two people
                    res += 1
                    j -= 1  # back
                    i += 1  # go
                else:  # one person only
                    res += 1
                    j -= 1  # back
        return res


"""
Runtime: 616 ms, faster than 13.33% of Python3 online submissions for Boats to Save People.
Memory Usage: 19.6 MB, less than 16.67% of Python3 online submissions for Boats to Save People.
"""


"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
