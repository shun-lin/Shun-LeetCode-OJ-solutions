# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None):
            return False;
        slow = head;
        fast = head;
        while (fast != None and slow != None):
            fast = fast.next;
            if (fast == None):
                return False;
            fast = fast.next;
            if (fast == None):
                return False;
            slow = slow.next;
            if (slow == fast):
                return True;
