"""
@Title: 1010. Pairs of Songs With Total Durations Divisible by 60
@Tag: array / math
@Date: Feb-08 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def numPairsDivisibleBy60(self, T: List[int]) -> int:
        freq, res = [0] * 60, 0
        for t in T:  # count the freq
            freq[t % 60] += 1
        for i in range(31):  # check "0 - 30"(-th)
            if (i == 0 or i == 30):  # e.g: 60, 180, 360  /  30, 90, 120
                n = freq[i]
                res += n * (n - 1) // 2  # combination (pick two of them up)
            else:
                res += freq[i] * freq[60 - i]  # permutation
        return res


"""
Runtime: 224 ms, faster than 98.30% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
Memory Usage: 16.5 MB, less than 9.09% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
"""
