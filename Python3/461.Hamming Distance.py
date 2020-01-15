"""
@Title: 461. Hamming Distance
@Tag: bit shifting
@Date: Jan-15 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


"""
Runtime: 28 ms, faster than 61.17% of Python3 online submissions for Hamming Distance.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Hamming Distance.
"""


"""
Thanks to:  @yuyuyu0905
https://leetcode.com/problems/hamming-distance/discuss/94697/Python-1-line-49ms
"""
