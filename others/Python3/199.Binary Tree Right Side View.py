"""
@Title: 199. Binary Tree Right Side View
@Tag: binary tree
@Date: Mar-06 2020
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue, res = [root], []
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == n - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


"""
Runtime: 28 ms, faster than 80.95% of Python3 online submissions for Binary Tree Right Side View.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Right Side View.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
