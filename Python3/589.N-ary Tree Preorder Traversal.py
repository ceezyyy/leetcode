"""
@Title: 589. N-ary Tree Preorder Traversal
@Tag: N-ary tree
@Date: Jan-19 2020
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
        stack, res = [], []
        if not root:  # corner case
            return stack
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack += [child for child in node.children[::-1] if node.children]
        return res


"""
Runtime: 52 ms, faster than 53.10% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
