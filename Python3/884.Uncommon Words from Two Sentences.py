"""
@Title: 884. Uncommon Words from Two Sentences
@Tag: HashTable
@Date: Nov-12    2019
@Author: ceezyyy
@Difficulty: Easy
"""

from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        res = []
        C = A+' '+B  # the combination of A & B
        d = {item: {'occurrence': 0} for item in C.split()}  # HashTable
        # frequency of occurrence
        for word in C.split():
            d[word]['occurrence'] += 1
        for word in d:
            if d[word]['occurrence'] < 2:
                res.append(word)
        return res


def test():
    s = Solution()
    res = s.uncommonFromSentences("this apple is sweet", "this apple is sour")
    print(res)


if __name__ == "__main__":
    test()


"""
Runtime: 16 ms, faster than 99.86% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Uncommon Words from Two Sentences.
"""
