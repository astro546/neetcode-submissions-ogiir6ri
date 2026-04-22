# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First, we create a dummy node that points to the head of the linked list
        dummy = ListNode(None, head)

        #Then, we define fast(right), and slow(left), pointers at dummy node
        f = s = dummy

        # First, we create the gap between f and s of size n
        for i in range(n):
            f = f.next

        # Then, we move f and s at the same time, until f reaches the end of the linked list
        # When f reaches the end, s will be in the nth node from the end
        while f and f.next:
            f = f.next
            s = s.next
        
        # Finally, remove the nth node, by making the (n-1)th node points to s.next.next
        s.next = s.next.next

        # We return dummy.next, beacuse, if we remove the only single node in the linked list,
        # the linked list will get empty, so, we use the dummy node to points a null node, that means,
        # the linked list is now empty
        return dummy.next