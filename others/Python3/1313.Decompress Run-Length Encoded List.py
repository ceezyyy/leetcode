"""
@Title: 1313. Decompress Run-Length Encoded List
@Tag: array
@Date: Feb-06 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res, n = [], len(nums)
        for i in range(1, n, 2):
            temp = [nums[i]] * nums[i-1]
            res.extend(temp)
        return res


"""
Runtime: 68 ms, faster than 71.87% of Python3 online submissions for Decompress Run-Length Encoded List.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
