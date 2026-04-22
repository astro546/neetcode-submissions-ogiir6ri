# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        f = s = dummy
        for i in range(n):
            f = f.next

        while f and f.next:
            f = f.next
            s = s.next
            
        s.next = s.next.next
        return dummy.next