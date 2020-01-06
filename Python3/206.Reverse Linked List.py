"""
@Title: 206. Reverse Linked List
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
    def reverseList(self, head: ListNode) -> ListNode:  # a utility problem
        pre = None  # previous node
        cur = head  # current node
        while cur:  # iteratively
            nxt = cur.next  # save the next node
            cur.next = pre  # reverse
            # go ahead
            pre = cur
            cur = nxt
        return pre


"""
Runtime: 36 ms, faster than 46.08% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
