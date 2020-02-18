"""
@Title: 002. Add Two Numbers
@Tag: linked list
@Date: Feb-18 2020
@Author: ceezyyy
@Difficulty: Medium
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:  # corner case
            return None
        D = self.int2list(self.list2int(l1) + self.list2int(l2))
        if not D:  # corner case
            return ListNode(0)
        res = cur = ListNode(D[0])
        for i in range(1, len(D)):
            cur.next = ListNode(D[i])
            cur = cur.next
        return res

    def list2int(self, L):
        """
        convert linked-list to int
        """
        cnt, res = 0, 0
        cur = L
        while cur:
            res += pow(10, cnt) * cur.val
            cur = cur.next
            cnt += 1
        return res

    def int2list(self, k):
        """
        convert int to list
        """
        res = []
        while k:
            res.append(k % 10)
            k //= 10
        return res


"""
Runtime: 76 ms, faster than 30.05% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
"""
