"""
@Title: 101. Symmetric Tree
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:  # corner case
            return True
        return self.helper(root.left, root.right)

    def helper(self, p, q) -> bool:
        if not p and not q:  # base case 1
            return True
        elif not p or not q:  # base case 2
            return False
        elif p.val != q.val:  # base case 3
            return False
        else:
            return self.helper(p.left, q.right) and self.helper(p.right, q.left)


"""
Runtime: 32 ms, faster than 69.87% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
