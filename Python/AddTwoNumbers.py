# You are given two non-empty linked lists representing two non-negative integers.

# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None):
            return None;
        result = ListNode(0);
        carry_over = 0;
        num = l1.val + l2.val;
        if (num >= 10):
            carry_over = 1;
            num -= 10;
        result.val = num;
        result_copy = result;
        while (l1.next != None or l2.next != None):
            result_copy.next = ListNode(0);
            result_copy = result_copy.next;
            if (l1.next == None):
                l2 = l2.next;
                num = l2.val + carry_over;
                carry_over = 0;
                if (num >= 10):
                    carry_over = 1;
                    num -= 10;
                result_copy.val = num;
            elif (l2.next == None):
                l1 = l1.next;
                num = l1.val + carry_over;
                carry_over = 0;
                if (num >= 10):
                    carry_over = 1;
                    num -= 10;
                result_copy.val = num;
            else:
                l1 = l1.next;
                l2 = l2.next;
                num = l1.val + l2.val + carry_over;
                carry_over = 0;
                if (num >= 10):
                    carry_over = 1;
                    num -= 10;
            result_copy.val = num;
        if (carry_over == 1):
            result_copy.next = ListNode(1);
        return result;
