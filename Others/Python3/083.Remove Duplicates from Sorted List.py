"""
@Title: 083. Remove Duplicates from Sorted List
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next  # delete duplicate
            else:  # 'else' here is crucial!
                cur = cur.next  # go ahead
        return head


"""
Runtime: 36 ms, faster than 85.50% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
