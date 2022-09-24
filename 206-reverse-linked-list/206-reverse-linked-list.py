# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        tempPrev = head
        cur = head.next
        head.next = None
        while cur != None:
            tempNext = cur.next
            cur.next = tempPrev
            tempPrev = cur
            cur = tempNext
        
        return tempPrev
            