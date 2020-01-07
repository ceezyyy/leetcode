"""
@Title: 203. Remove Linked List Elements
@Tag: linked list
@Date: Jan-07 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # corner case
        if not head:
            return None
        pre_node = ListNode(-1)  # the imaginary node
        pre_node.next = head
        cur = pre_node
        while cur.next:  # scan
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return pre_node.next  # do not return 'head' or 'cur'


"""
Runtime: 60 ms, faster than 93.34% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Remove Linked List Elements.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
