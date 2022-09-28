# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeMap = {}
        
        curr = head
        
        while curr != None:
            if curr in nodeMap:
                return True
            else:
                nodeMap[curr] = 1
            
            curr = curr.next
        
        return False