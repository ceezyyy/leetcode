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
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


"""
Runtime: 52 ms, faster than 8.70% of Python3 online submissions for Fizz Buzz.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
