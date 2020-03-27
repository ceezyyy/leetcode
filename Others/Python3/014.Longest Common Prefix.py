"""
@Title: 014. Longest Common Prefix
@Tag: str
@Date: Jan-05 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # corner case
        if not strs:
            return res
        if len(strs) == 1:
            return strs[0]
        min_len = len(strs[0])
        # find the minimumn length of the word in order not to out of bound
        for cur_word in strs:
            min_len = len(cur_word) if len(cur_word) < min_len else min_len
        for index in range(min_len):
            for k in range(1, len(strs)):
                if strs[k][index] != strs[k-1][index]:  # make no sense
                    return res  # return the res immediately
                else:  # make sense
                    if k == len(strs) - 1:  # the last word
                        res += strs[k][index]
        return res


"""
Runtime: 24 ms, faster than 96.71% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
"""


"""
Time Complexity: O(n*n)
Space Complexity: O(1)
"""
