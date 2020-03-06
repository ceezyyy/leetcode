"""
@Title: 515. Find Largest Value in Each Tree Row
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
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], [root]
        while queue:  # BFS
            n = len(queue)
            temp = float("-inf")
            for i in range(n):
                node = queue.pop(0)
                temp = node.val if node.val > temp else temp  # keep tracking the max
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res


"""
Runtime: 40 ms, faster than 92.57% of Python3 online submissions for Find Largest Value in Each Tree Row.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Find Largest Value in Each Tree Row.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
