"""
@Title: 144. Binary Tree Preorder Traversal
@Tag: binary tree
@Date: Mar-05 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Approach 1: (Iterative)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # preorder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res


"""
Runtime: 20 ms, faster than 96.33% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


# Approach 2: (Recursive)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if node:
            res.append(node.val)
            self.dfs(node.left, res)
            self.dfs(node.right, res)


"""
Runtime: 20 ms, faster than 96.27% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
