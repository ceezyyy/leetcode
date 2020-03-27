"""
@Title: 019. Remove Nth Node From End of List
@Tag: linked list
@Date: Jan-20 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Two Pass
        if not head:  # corner case
            return None
        dummy = pre = ListNode(float("-inf"))  # dummy node
        dummy.next, length, loc = head, 0, 0  # initialization
        while pre.next:  # get the length of the linked list
            pre = pre.next  # go ahead
            length += 1
        pre = dummy  # "reset"
        while pre.next:  # find the location
            if loc == length - n:  # key point
                pre.next = pre.next.next
                break
            else:
                pre = pre.next
                loc += 1
        return dummy.next


"""
Runtime: 24 ms, faster than 94.75% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
