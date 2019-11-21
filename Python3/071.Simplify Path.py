"""
@Title: 071. Simplify Path
@Tag: stack str
@Date: Nov-21 2019
@Author: ceezyyy
@Difficulty: Medium
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')
        # input
        for path in paths:
            if not path or path == '.':  # current dir
                continue
            elif path == '..':  # move a dir up a level
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(path)
        # optput
        # note that the returned canonical path must always begin with a slash /
        return '/'+'/'.join(stack)


def test():
    s = Solution()
    res = s.simplifyPath("/a//b////c/d//././/..")
    print(res)


if __name__ == "__main__":
    test()


"""
Study Notes:

1. join(): The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.

2.split(): Return a list of the words in the string, using sep as the delimiter string.

"""


"""
Runtime: 28 ms, faster than 96.70% of Python3 online submissions for Simplify Path.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Simplify Path.
"""
