"""
@Title: 237. Delete Node in a Linked List
@Tag: linked list
@Date: Jan-06 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val, node.next.val = node.next.val, node.val  # swap
            if node.next.next == None:  # last but one
                node.next = None  # in-place
            else:
                node = node.next  # walk through until reach the end


"""
Runtime: 40 ms, faster than 27.25% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Delete Node in a Linked List.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
