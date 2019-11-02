"""
@Title: 242. Valid Anagram
@Tag: str
@Date: Nov-02 2019
@Author: ceezyyy
@Difficulty: Easy
"""

# Solution One


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)


def test():
    s = Solution()
    print(s.isAnagram("rat", "tar"))


if __name__ == "__main__":
    test()


'''
Runtime: 44 ms, faster than 93.31% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.3 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
'''
