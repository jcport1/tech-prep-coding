# https://leetcode.com/problems/min-stack/
class MinStack:

    # time complexity: O(1) for each operation

    """ approach: create two stacks -> standard stack and minStack (to keep track of min)
    each "level" of the minStack is keeping track of min (which could be a given val that is pushed to stack)
    when we pop from the main stack, we also pop from minStack (because new min could be updated and each current level
    keeps track of minimum at given time)
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # add min value to minStack
        # first check that minStack is not empty, otherwise use val
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()