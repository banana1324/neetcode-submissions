# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        firstToLast = []
        curr = head.next

        while curr:
            firstToLast.append(curr)
            curr= curr.next

        left = 0
        right = len(firstToLast)-1

        while left <= right:
            head.next = firstToLast[right]
            head = head.next
            head.next = firstToLast[left]
            head = head.next
            left += 1
            right -= 1
        head.next = None
        return None
