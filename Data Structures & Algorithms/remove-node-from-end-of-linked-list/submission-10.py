# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        poo = ListNode()
        poopoo= ListNode()
        poo.next = head
        poopoo.next = poo
        fast = poo
        slow = poo

        for _ in range(n):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
            poopoo = poopoo.next
        poopoo.next = slow.next
        
        if poopoo == head:
            return poopoo
        if slow == head:
            return poopoo.next
        return head



#                  ___ ___ 9 0 3 8 7 3 8 6 3 1