# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cont = head.next.next
        new_head = head.next
        new_head.next = head
        new_head.next.next = self.swapPairs(cont)
        return new_head