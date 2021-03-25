"""
@Title: 1302. Deepest Leaves Sum
@Tag: binary tree
@Date: Feb-13 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res, queue = [], []
        if not root:
            return 0
        queue.append(root)
        while queue:
            size = len(queue)  # the size of each level
            temp = []
            while size:  # each level
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
                temp.append(node.val)
            res.append(temp)
        return sum(res[-1])


"""
Runtime: 100 ms, faster than 53.48% of Python3 online submissions for Deepest Leaves Sum.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Deepest Leaves Sum.
"""
