# Merge in between liked lists problem: https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = current = tmp = list1
        end = None
        
        while True:
            if tmp is not None:
                if tmp.val == a - 1:
                    tmp = current.next
                    current.next = list2
                elif tmp.val == b + 1:
                    end = tmp
                tmp = tmp.next
            if current.next is None:
                if tmp is not None:
                    continue
                else:
                    current.next = end
                    return head
            current = current.next
