"""
@Title: 590. N-ary Tree Postorder Traversal
@Tag: tree
@Date: Oct-28 2019
@Author: ceezyyy
@Difficulty: Easy
"""


from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)  # 'root' is also a paramete
        return res


"""
Runtime: 644 ms, faster than 94.72% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 95.2 MB, less than 7.14% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
