"""
@Title: 1346. Check If N and Its Double Exist
@Tag: array
@Date: Feb-09 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        for a in arr:
            if a < 0:
                if a / 2 in arr:
                    return True
            if a > 0:
                if a * 2 in arr:
                    return True
            if a == 0:
                if arr.count(0) >= 2:
                    return True
        return False


"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
