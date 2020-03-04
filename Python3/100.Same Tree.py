"""
@Title: 100. Same Tree
@Tag: binary tree
@Date: Mar-04 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  # base case 1
            return True
        elif not p or not q:  # base case 2
            return False
        elif p.val != q.val:  # base case 3
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
Runtime: 28 ms, faster than 69.59% of Python3 online submissions for Same Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Same Tree.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
