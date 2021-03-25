"""
@Title: 021. Merge Two Sorted Lists
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)  # a dummy node
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:  # sorted
                cur.next = l1
                l1 = l1.next  # go ahead
            else:
                cur.next = l2
                l2 = l2.next  # go ahead
            cur = cur.next  # go ahead
        # when one of them is None, cur should point at the remainder since the linked lists are sorted
        cur.next = l1 if l1 else l2
        return dummy.next


"""
Runtime: 36 ms, faster than 52.71% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
