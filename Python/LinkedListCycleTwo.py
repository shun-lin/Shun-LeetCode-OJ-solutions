# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return None;
        slow = head;
        fast = head;
        while (slow != None and fast != None):
            fast = fast.next;
            if (fast == None):
                return None;
            fast = fast.next;
            slow = slow.next;
            if (slow == fast):
                break;
        if (fast == None):
            return None;
        slow = head;
        while (slow != fast):
            slow = slow.next;
            fast = fast.next;
        return slow;
