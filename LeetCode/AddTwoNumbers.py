# Add Two Numbers problem: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = head = ListNode(0)
        remainder = 0
        
        while l1 is not None or l2 is not None:    
            l1_val = 0
            l2_val = 0
            
            if l1:
                l1_val = l1.val
                l1 = l1.next
            
            if l2:
                l2_val = l2.val
                l2 = l2.next
            
            addition = l1_val + l2_val + remainder
            
            if addition >= 10:
                remainder = addition // 10
                addition = addition % 10
            else:
                remainder = 0
            
            current.next = ListNode(addition)
            current = current.next
        
        if remainder > 0:
            current.next = ListNode(remainder)
        
        return head.next