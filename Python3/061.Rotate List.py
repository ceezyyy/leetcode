"""
@Title: 061. Rotate List
@Tag: linked list
@Date: Feb-19 2020
@Author: ceezyyy
@Difficulty: Medium
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n, temp = 0, []
        cur = head
        while cur:
            n += 1  # length
            temp.append(cur.val)
            cur = cur.next
        res = [0] * n
        for i, v in enumerate(temp):  # rotate
            res[(i+k) % n] = v
        cur, n = head, 0
        while cur:
            cur.val = res[n]
            cur = cur.next
            n += 1
        return head


"""
Runtime: 32 ms, faster than 84.00% of Python3 online submissions for Rotate List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rotate List.
"""


"""
Time Complexity: o(n)
Space Complexity: O(n)
"""
