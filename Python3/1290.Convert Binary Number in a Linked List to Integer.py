"""
@Title: 1290. Convert Binary Number in a Linked List to Integer
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
    def getDecimalValue(self, head: ListNode) -> int:
        arr, str_arr = [], ""
        while head:  # linked list to array
            arr.append(head.val)
            head = head.next
        arr = list(map(str, arr))  # list of int -> list of str
        str_arr = "".join(arr)  # list of str -> str
        return int(str_arr, 2)  # str -> int


"""
Runtime: 28 ms, faster than 66.55% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
