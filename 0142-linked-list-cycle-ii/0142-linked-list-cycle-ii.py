# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return None 
        slowPointer, fastPointer = head, head
        
        while True:
            slowPointer = slowPointer.next
            
            fastPointer = fastPointer.next
            if fastPointer == None:
                break
            fastPointer = fastPointer.next
            
            if slowPointer == fastPointer or fastPointer == None:
                break
        
        if (fastPointer == None):
            return None
        
        headPointer = head
        
        while headPointer != slowPointer:
            headPointer = headPointer.next
            slowPointer = slowPointer.next
        
        return slowPointer