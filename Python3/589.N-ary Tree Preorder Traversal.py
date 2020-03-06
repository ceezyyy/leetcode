"""
@Title: 589. N-ary Tree Preorder Traversal
@Tag: N-ary tree
@Date: Feb-06 2020
@Author: ceezyyy
@Difficulty: Easy
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend([child for child in node.children][::-1])
        return res


"""
Runtime: 52 ms, faster than 58.70% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
