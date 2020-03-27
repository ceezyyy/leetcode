"""
@Title: 1078. Occurrences After Bigram
@Tag: str
@Date: Nov-05 2019
@Author: ceezyyy
@Difficulty: Easy
"""

from typing import List


class Solution:
    def findOccurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        # str.split(separator, maxsplit)
        text = text.split()  # <class 'list'>
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                res.append(text[i+2])
        return res


def test():
    s = Solution()
    res = s.findOccurrences("we will we will rock you", "we", "will")
    print(res)


if __name__ == "__main__":
    test()
