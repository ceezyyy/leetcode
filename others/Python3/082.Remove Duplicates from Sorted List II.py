"""
@Title: 082. Remove Duplicates from Sorted List II
@Tag: linked list
@Date: Jan-11 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # corner case
        if not head:
            return None
        dummy = pre = ListNode(-1)  # a dummy node
        pre.next = head  # two pointers
        while head and head.next:
            if head.val == head.next.val:  # duplicate
                while head and head.next and head.val == head.next.val:  # core
                    head = head.next  # keep going ahead
                head = head.next  # one more step, 'remove' itself
                pre.next = head  # point at
            else:  # go ahead
                pre = pre.next
                head = head.next
        return dummy.next


"""
Runtime: 36 ms, faster than 83.20% of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List II.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
