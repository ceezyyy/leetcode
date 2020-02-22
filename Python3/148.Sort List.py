"""
@Title: 148. Sort List
@Tag: linked-list / sort
@Date: Feb-22 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        cur, res = head, []
        while cur:
            res.append(cur.val)
            cur = cur.next
        res, cur = sorted(res), head
        while cur:
            cur.val = res.pop(0)
            cur = cur.next
        return head


"""
Runtime: 160 ms, faster than 85.63% of Python3 online submissions for Sort List.
Memory Usage: 20.1 MB, less than 100.00% of Python3 online submissions for Sort List.
"""


"""
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
