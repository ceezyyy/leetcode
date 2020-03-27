"""
@Title: 513. Find Bottom Left Tree Value
@Tag: binary Tree
@Date: Oct-23 2019
@Author: ceezyyy
@Difficulty: Medium 
"""


from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        # level order
        q = deque()  # q is a dequeue (from left->right)
        res = []
        # You may assume the tree (i.e., the given root node) is not NULL
        q.append(root)  # the first element (left->right)
        while q:
            temp = []
            size = len(q)
            # Remove and return an element from the left side of the deque.
            # If no elements are present, raises an
            for i in range(size):
                node = q.popleft()  # from the left (the front of the queue)
                temp.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            res.append(temp)
        return res[-1][0]


"""
Runtime: 48 ms, faster than 88.54% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 16.3 MB, less than 33.33% of Python3 online submissions for Find Bottom Left Tree Value.
"""
