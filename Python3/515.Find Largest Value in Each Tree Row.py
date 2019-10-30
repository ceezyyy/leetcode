"""
@Title: 515. Find Largest Value in Each Tree Row
@Tag: binary tree
@Date: Oct-28 2019
@Author: ceezyyy
@Difficulty: Medium
"""

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # level order
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            temp = []
            size = len(queue)
            for i in range(size):  # each level
                node = queue.pop(0)  # the front of the queue
                if(node.left):  # left child
                    queue.append(node.left)
                if(node.right):  # right child
                    queue.append(node.right)
                temp.append(node.val)
            res.append(max(temp))
        return res
