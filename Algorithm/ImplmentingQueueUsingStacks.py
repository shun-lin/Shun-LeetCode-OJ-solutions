class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # stack is first in last out so in python we can use append to add and
        # pop front

        # we want to implement a queue which is first in first out
        self.stacks = [[], []]
        self.activeStackIndex = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        otherStateIndex = 1 - self.activeStackIndex
        while len(self.stacks[self.activeStackIndex]) > 0:
            lastElement = self.stacks[self.activeStackIndex].pop()
            self.stacks[otherStateIndex].append(lastElement)
        self.stacks[otherStateIndex].append(x)
        while len(self.stacks[otherStateIndex]) > 0:
            lastElement = self.stacks[otherStateIndex].pop()
            self.stacks[self.activeStackIndex].append(lastElement)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stacks[self.activeStackIndex].pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        lastElementInex = len(self.stacks[self.activeStackIndex]) - 1
        return self.stacks[self.activeStackIndex][lastElementInex]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stacks[self.activeStackIndex]) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
