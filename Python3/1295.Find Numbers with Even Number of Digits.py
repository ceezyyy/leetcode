"""
@Title: 1295. Find Numbers with Even Number of Digits
@Tag: array
@Date: Jan-02 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            digit = 0  # the digit of each number
            while nums[i] > 0:
                nums[i] = nums[i] // 10
                digit += 1
            if digit % 2 == 0:  # even number of digit
                res += 1
        return res


"""
Runtime: 52 ms, faster than 72.51% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
