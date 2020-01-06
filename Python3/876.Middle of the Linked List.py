"""
@Title: 876. Middle of the Linked List
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
    def middleNode(self, head: ListNode) -> ListNode:
        # corner case
        if not head:
            return None
        slow = head  # the slow pointer
        fast = head  # the fast pointer
        while fast and fast.next:
            # time is the same, but the speed of 'fast pointer' is twice as much as 'slow pointer',
            # so when 'fast pointer' reach the end, 'slow pointer' just reach the middle
            fast = fast.next.next  # if not fast: None
            slow = slow.next
        return slow


"""
Runtime: 24 ms, faster than 83.45% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Middle of the Linked List.
"""


"""
Time Complexity: O(n/2) -> O(n)
Space Complexity: O(1)
"""
