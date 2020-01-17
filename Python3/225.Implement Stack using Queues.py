"""
@Title: 225. Implement Stack using Queues
@Tag: stack
@Date: Jan-17 2020
@Author: ceezyyy
@Difficulty: Easy
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


"""
Runtime: 24 ms, faster than 82.64% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Implement Stack using Queues.
"""
