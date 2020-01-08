"""
@Title: 141. Linked List Cycle
@Tag: linked list
@Date: Jan-08 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        while cur:
            if cur.val == None:
                return True
            else:
                cur.val = None
                cur = cur.next
        return False


"""
Runtime: 48 ms, faster than 63.49% of Python3 online submissions for Linked List Cycle.
Memory Usage: 15.7 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
