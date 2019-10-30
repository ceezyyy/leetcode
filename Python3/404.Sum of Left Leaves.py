"""
@Title: 404. Sum of Left Leaves
@Tag: binary tree
@Date: Oct-30 2019
@Author: ceezyyy
@Difficulty: Easy
"""


from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        self.isLeftLeaves(root.left, True, res)  # remember to add "self."
        self.isLeftLeaves(root.right, False, res)
        return sum(res)

    def isLeftLeaves(self, node: TreeNode, isLeft: bool, res: List) -> None:
        if not node:
            return
        # is a leaf node
        if not node.left and not node.right and isLeft:  # is the left leaf
            res.append(node.val)
        self.isLeftLeaves(node.left, True, res)
        self.isLeftLeaves(node.right, False, res)


"""
Runtime: 36 ms, faster than 88.71% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.4 MB, less than 7.69% of Python3 online submissions for Sum of Left Leaves.
"""
