# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dumbo = ListNode()
        dumbo.next = head
        curr = head
        prev=dumbo
        prev.next = curr
        currInd = 1
        while currInd < left:
            curr = curr.next
            prev = prev.next
            currInd += 1

        beforeLeft = prev
        revstart = curr

        #rev algo from left to right
        while currInd <= right:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            currInd += 1
        

        beforeLeft.next = prev
        revstart.next = curr
        return dumbo.next
        









