"""
@Title: 653. Two Sum IV - Input is a BST
@Tag: binary tree & two pointers
@Date: Oct-29 2019
@Author: ceezyyy
@Difficulty: Easy
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # BFS
        if not root:
            return False
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            for i in range(size):  # each level
                node = queue.pop(0)  # the front element of queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                res.append(node.val)
        res.sort()  # from small -> large
        # two pointers
        i = 0  # left pointer
        j = len(res)-1  # right pointer
        while i < j:
            if res[i]+res[j] == k:
                return True
            else:
                if res[i]+res[j] < k:
                    i += 1
                else:
                    j -= 1
        return not i == j


"""
Runtime: 96 ms, faster than 42.77% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 15.9 MB, less than 11.76% of Python3 online submissions for Two Sum IV - Input is a BST.
"""
