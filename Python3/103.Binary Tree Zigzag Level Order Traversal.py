"""
@Title: 103. Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res = [root], []
        while queue:
            n, level = len(queue), []
            for i in range(n):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        for i, r in enumerate(res):
            if i % 2 != 0:
                res[i] = res[i][::-1]
        return res


"""
Runtime: 28 ms, faster than 82.40% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
