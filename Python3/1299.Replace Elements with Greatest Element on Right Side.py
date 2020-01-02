"""
@Title: 1299. Replace Elements with Greatest Element on Right Side
@Tag: array
@Date: Jan-02 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = arr[-1]  # initialization
        for i in range(len(arr)-2, -1, -1):  # traverse backward
            temp = arr[i]
            arr[i] = right_max  # in-place
            # the greatest element among the elements to its right
            right_max = temp if temp > right_max else right_max
        arr[-1] = -1  # replace the last element with -1
        return arr


"""
Runtime: 80 ms, faster than 75.23% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
