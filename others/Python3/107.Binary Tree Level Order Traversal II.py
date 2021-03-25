"""
@Title: 107. Binary Tree Level Order Traversal II
@Tag: binary tree
@Date: Mar-01 2020
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:  # corner case
            return []
        queue, res = [root], []
        while queue:  # "still waiting in line"
            level, n = [], len(queue)
            for i in range(n):
                cur = queue.pop(0)  # pop the first element each time
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        return res[::-1]


"""
Runtime: 24 ms, faster than 97.88% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
