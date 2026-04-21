# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
        
        curr = s.next
        s.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        f = head
        s = prev
        while s:
            tmp1 = f.next
            tmp2 = s.next

            f.next = s
            s.next = tmp1

            f = tmp1
            s = tmp2

        

        