"""
@Topic: 022. Generate Parentheses
@Tag: recursion/
@Date: Dec-13 2019
@Author: ceezyyy
@Difficulty: Medium 
"""


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []  # the final result
        self.dfs(n, n, "", res)  # magic function(recursive)
        return res

    def dfs(self, left: int, right: int, cur: str, res: List[str]) -> None:
        if left > right:  # constraints
            return
        if left == 0 and right == 0:  # the exit of recursion: when to stop
            res.append(cur)
        else:  # the choice "(" or ")"
            if left > 0:
                self.dfs(left-1, right, cur+"(", res)
            if right > 0:
                self.dfs(left, right-1, cur+")", res)


"""
Runtime: 36 ms, faster than 74.71% of Python3 online submissions for Generate Parentheses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Generate Parentheses.
"""


"""
Study Notes:
Generate All Strings With n Matched Parentheses - YouTube
https://www.youtube.com/watch?v=sz1qaKt0KGQ

"""
