"""
@Title: 155. Min Stack
@Tag: stack
@Date: Oct-24 2019
@Author: ceezyyy
@Difficulty: Easy
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # Lists are used as stacks
        # stack[x,y]
        # x stands for the current value
        # y stands for the latest minimum value

    def push(self, x: int) -> None:
        # 'list' object has no attribute 'push'
        if not self.stack:
            self.stack.append([x, x])
        else:
            # the latest minimum
            self.stack.append([x, min(x, self.stack[-1][-1])])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]


def test():
    minstack = MinStack()
    minstack.push(5)
    minstack.push(4)
    minstack.push(3)
    minstack.push(2)
    minstack.push(1)
    minstack.pop()
    print(minstack.top())
    print(minstack.getMin())


if __name__ == "__main__":
    test()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
Runtime: 68 ms, faster than 91.97% of Python3 online submissions for Min Stack.
Memory Usage: 17.8 MB, less than 5.36% of Python3 online submissions for Min Stack.
"""
