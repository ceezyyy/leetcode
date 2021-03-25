"""
@Title: 222. Count Complete Tree Nodes
@Tag: binary tree
@Date: Mar-09 2020
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
    def countNodes(self, root: TreeNode) -> int:
        # level order
        if not root:
            return 0
        queue, res = [root], 0
        while queue:
            n = len(queue)  # the number of nodes in current level
            res += n
            for i in range(n):  # nodes in current level
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


"""
Runtime: 124 ms, faster than 9.38% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 20.2 MB, less than 100.00% of Python3 online submissions for Count Complete Tree Nodes.
"""


"""
Time Complexity: O(n)
Space Complexity: O(h)
"""
