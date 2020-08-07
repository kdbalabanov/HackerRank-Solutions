# Convert binary in linked list to integer problem: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        num = 0
        
        while head is not None:
            l.append(head.val)
            head = head.next
            
        length = len(l)
        
        for i in range(0, length):
            num += l[i] * (2 ** (length - i - 1))
        
        return num
