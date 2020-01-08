"""
@Title: 160. Intersection of Two Linked Lists
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()  # store the nodes which have been visited
        while headA:  # walk through headA
            visited.add(headA)  # the node is already visited
            headA = headA.next
        while headB:  # walk through headB
            if headB in visited:  # the intersection we are looking for
                return headB
            headB = headB.next
        return None  # no intersection


"""
Runtime: 172 ms, faster than 37.98% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 28.4 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
