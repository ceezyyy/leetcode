"""
@Title: 234. Palindrome Linked List
@Tag: linked list
@Date: Jan-09 2020
@Author: ceezyyy
@Difficulty: Easy
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr, cur = [], head
        while cur:  # linked list -> array
            arr.append(cur.val)
            cur = cur.next  # go ahead
        return arr == arr[::-1]


"""
Runtime: 68 ms, faster than 73.41% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 22.9 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
