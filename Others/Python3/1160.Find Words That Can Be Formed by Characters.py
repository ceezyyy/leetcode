"""
@Title: 1160. Find Words That Can Be Formed by Characters
@Tag: string 
@Date: Jan-28 2020
@Author: ceezyyy
@Difficulty: Easy
"""


import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            if all(collections.Counter(word)[ch] <= collections.Counter(chars)[ch] for ch in word):
                res += len(word)
        return res


"""
To form a string using characters from chars, the frequency of each character in chars must be greater than or equal the frequency of that character in the string to be formed.
"""


"""
Python all() Function
The all() function returns True if all items in an iterable are true, otherwise it returns False. If the iterable object is empty, the all() function also returns True.
"""
