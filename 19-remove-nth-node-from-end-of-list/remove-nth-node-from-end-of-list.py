# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow
        slow = slow.next
        temp.next = slow.next
        slow.next = None

        return head
