"""
@Title: 102. Binary Tree Level Order Traversal
@Tag: binary tree
@Date: Mar-01 2020
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []
        res, queue = [], [root]
        while queue:  # "still waiting in line"
            level, n = [], len(queue)
            for i in range(n):
                # pop the first element in the queue each time
                node = queue.pop(0)
                level.append(node.val)
                if node.left:  # check left child
                    queue.append(node.left)
                if node.right:  # check right child
                    queue.append(node.right)
            res.append(level)
        return res


"""
Runtime: 28 ms, faster than 91.54% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
