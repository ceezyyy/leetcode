"""
@Title: 328. Odd Even Linked List
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        # corner case
        if not head:
            return None
        even_head = head.next
        odd, even = head, even_head  # two pointers: odd & even
        while odd.next and even.next:
            # 'odd' first in order to eliminate the effects of 'even' pointers
            odd.next = odd.next.next
            odd = odd.next  # go ahead
            even.next = even.next.next
            even = even.next  # go ahead
        odd.next = even_head  # tail of 'odd' -> head of 'even'
        return head


"""
Runtime: 44 ms, faster than 37.72% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
