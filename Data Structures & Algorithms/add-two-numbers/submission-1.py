# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = False

        while l1 or l2:            
            dig1 = 0
            dig2 = 0

            if l1:
                dig1 = l1.val
            if l2:
                dig2 = l2.val

            total = dig1 + dig2

            if carry:
                total += 1

            curr.val = total % 10
            carry = total >= 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next            
            if l1 or l2:
                curr.next = ListNode()
                curr = curr.next

        if carry == True and head:
            curr.next = ListNode(1)
        return head

