"""
@Title: 242. Valid Anagram
@Tag: str
@Date: Jan-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26  # the frequency of each letters
        if len(s) != len(t):  # s and t should have the same length
            return False
        for i in range(len(s)):
            freq[ord(s[i])-ord('a')] += 1
            freq[ord(t[i])-ord('a')] -= 1
        # all the element should be the same -- zero
        return len(set(freq)) == 1


"""
Runtime: 56 ms, faster than 25.61% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.1 MB, less than 96.88% of Python3 online submissions for Valid Anagram.
"""
