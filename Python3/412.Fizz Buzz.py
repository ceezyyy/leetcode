"""
@Title: 412. Fizz Buzz
@Tag: math
@Date: Jan-23 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i >= 3 and i % 3 == 0 and i >= 5 and i % 5 == 0:
                res.append("FizzBuzz")
                continue
            if i >= 3 and i % 3 == 0:
                res.append("Fizz")
                continue
            if i >= 5 and i % 5 == 0:
                res.append("Buzz")
                continue
            res.append(str(i))
        return res


"""
Runtime: 68 ms, faster than 5.61% of Python3 online submissions for Fizz Buzz.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
