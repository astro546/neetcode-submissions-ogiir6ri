# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We track the current, previous and next node.
        # We track the next the next node beacuase after execute the following steps,
        # The next node will not be able to be available from the current node
        # Also, we add a auxiliary node set to none at the start of the original linked list,
        # that is goiing to represent the end of the reversed liked list also.
        prev = None
        curr = head
        # Unitl  we reach the end of the original linked list
        while curr:
            # Store teh next node
            nxt = curr.next
            # connect the current node to the previous node
            curr.next = prev
            # move prev and curr pointers
            prev = curr
            curr = nxt
        return prev
        