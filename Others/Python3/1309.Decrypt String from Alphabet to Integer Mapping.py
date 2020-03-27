"""
@Title: 1309. Decrypt String from Alphabet to Integer Mapping
@Tag: string
@Date: Jan-26 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        res, i = [], len(s) - 1  # res: list[str], i: pointer
        while i >= 0:  # here "while" instead of "for" in order to better move our pointer
            if s[i] == "#":  # check s[i-2:i]
                res.append(chr(97 + int(s[i-2:i]) - 1))  # mapping
                i -= 3  # backwards
            else:
                res.append(chr(97 + int(s[i]) - 1))  # mapping
                i -= 1  # backwards
        return "".join(res[::-1])  # convert list[str] to str


"""
Runtime: 28 ms, faster than 72.49% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
