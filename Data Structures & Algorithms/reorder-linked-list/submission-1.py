# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(n), Space: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First, we put fast pointer to the last node,
        # And s into the middle of the linked list
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
        
        # Then, we are going to reverse the second half of the linked list
        curr = s.next
        s.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Finally, we merge the second half with the first half of the modified linked list
        f = head
        s = prev
        while s:
            tmp1 = f.next
            tmp2 = s.next

            f.next = s
            s.next = tmp1

            f = tmp1
            s = tmp2

        

        