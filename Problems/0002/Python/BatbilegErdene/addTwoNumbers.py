# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = ListNode((l1.val + l2.val)%10)
        carry = (l1.val + l2.val)//10
        current_node = sum
        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            current_node.next = ListNode((carry + l1.val + l2.val)%10)    
            carry = (carry + l1.val + l2.val) // 10
            current_node = current_node.next
        while(l1.next):
            l1 = l1.next
            current_node.next = ListNode((carry + l1.val)%10)    
            carry = (carry + l1.val) // 10
            current_node = current_node.next
        while(l2.next):
            l2 = l2.next
            current_node.next = ListNode((carry + l2.val)%10)    
            carry = (carry + l2.val) // 10
            current_node = current_node.next
        if carry > 0:
            current_node.next = ListNode(1)
        return sum