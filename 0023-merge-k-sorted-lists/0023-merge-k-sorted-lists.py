# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            newHead = dummyHead = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    dummyHead.next = list1
                    list1 = list1.next
                else:
                    dummyHead.next = list2
                    list2 = list2.next
                dummyHead = dummyHead.next

            if list1:
                dummyHead.next = list1
            if list2:
                dummyHead.next = list2
            return newHead.next
        
        newHead = lists[0]
        
        for i in range(1, len(lists)):
            newHead = mergeTwoLists(self, newHead, lists[i])
        
        return newHead
    
            