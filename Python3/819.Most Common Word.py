"""
@Title: 819. Most Common Word
@Tag: string 
@Date: Jan-27 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import string
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # remove all the punctuations from paragraph
        for punc in string.punctuation:
            paragraph = paragraph.replace(punc, " ")
        ban, res, most_freq = set(banned), "", 0
        # get the frequency of each element
        for word, freq in collections.Counter(paragraph.lower().split()).items():
            if word not in ban and freq > most_freq:
                res, most_freq = word, freq
        return res


"""
Runtime: 32 ms, faster than 68.47% of Python3 online submissions for Most Common Word.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Most Common Word.
"""
