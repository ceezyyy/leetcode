"""
@Title: 1346. Check If N and Its Double Exist
@Tag: array
@Date: Feb-09 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:  # corner case
            return True
        for a in set(sorted(arr)):
            if a < 0:  # negative
                if a / 2 in arr:
                    return True
            if a > 0:  # positive
                if a * 2 in arr:
                    return True
        return False


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
