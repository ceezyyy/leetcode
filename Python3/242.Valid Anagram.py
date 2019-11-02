"""
@Title: 242. Valid Anagram
@Tag: str
@Date: Nov-02 2019
@Author: ceezyyy
@Difficulty: Easy
"""

# Solution One(collections.Counter)


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)


'''
Runtime: 44 ms, faster than 93.31% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.3 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
'''


# Solution Two(HashTable)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # the first step
        res = [0]*26
        # HashTable
        for i, j in zip(s, t):  # zip() --> the length of the list should be the same
            res[ord(i)-97] += 1  # 'a'--97
            res[ord(j)-97] -= 1
        for i in range(len(res)):
            if res[i] != 0:
                return False
        return True


'''
Runtime: 64 ms, faster than 50.67% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.1 MB, less than 9.38% of Python3 online submissions for Valid Anagram.
'''


def test():
    s1 = Solution1()
    s2 = Solution2()
    print(s1.isAnagram("rat", "tar"))
    print(s2.isAnagram("a", "ab"))


if __name__ == "__main__":
    test()
