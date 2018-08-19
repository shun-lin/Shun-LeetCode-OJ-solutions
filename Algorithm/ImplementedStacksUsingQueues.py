class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queues = [[], []]
        self.activeQueueIndex = 0


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        otherStateIndex = 1 - self.activeQueueIndex
        self.queues[otherStateIndex].append(x)
        while len(self.queues[self.activeQueueIndex]) > 0:
            lastElement = self.queues[self.activeQueueIndex].pop(0)
            self.queues[otherStateIndex].append(lastElement)
        while len(self.queues[otherStateIndex]) > 0:
            lastElement = self.queues[otherStateIndex].pop(0)
            self.queues[self.activeQueueIndex].append(lastElement)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queues[self.activeQueueIndex].pop(0)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queues[self.activeQueueIndex][0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queues[self.activeQueueIndex]) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
