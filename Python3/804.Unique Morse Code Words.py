"""
@Title: 804. Unique Morse Code Words
@Tag: string
@Date: Jan-26 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping, res = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                        "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."], []
        for word in words:  # for loop
            temp = ""
            for ch in word:
                temp += mapping[ord(ch) - ord('a')]  # mapping
            res.append(temp)
        # here we use "set()" since it needs different transformations
        return len(set(res))


"""
Runtime: 36 ms, faster than 42.07% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Morse Code Words.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
