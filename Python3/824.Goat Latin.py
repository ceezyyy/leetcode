"""
@Title: 824. Goat Latin
@Tag: string 
@Date: Jan-29 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        index, vowels, res = 1, list("aeiouAEIOU"), []
        for word in S.split():
            if word[0] in vowels:  # rule one
                word += "ma"
            else:  # rule two
                word = word[1:] + word[0] + "ma"
            word += index * 'a'  # rule three
            index += 1
            res.append(word)
        return " ".join(res)


"""
Runtime: 28 ms, faster than 65.95% of Python3 online submissions for Goat Latin.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Goat Latin.
"""
