"""
@Title: 1305. All Elements in Two Binary Search Trees
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res, queue = [], []
        if root1:
            queue.append(root1)
        while queue:
            size = len(queue)
            temp = []
            while size:
                node = queue.pop(0)  # the first element
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
                res.append(node.val)
        queue = []
        if root2:
            queue.append(root2)
        while queue:
            size = len(queue)
            temp = []
            while size:
                node = queue.pop(0)  # the first element
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
                res.append(node.val)
        return sorted(res)


"""
Runtime: 340 ms, faster than 85.05% of Python3 online submissions for All Elements in Two Binary Search Trees.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for All Elements in Two Binary Search Trees.
"""
