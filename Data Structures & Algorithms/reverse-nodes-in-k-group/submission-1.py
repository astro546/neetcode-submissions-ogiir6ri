# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Time: O(N), Space: O(1)
class Solution:
   # This function reverse the current sublist
    def reverseList(self, groupNext, curr, prev):
        nxt = None
        while curr != groupNext:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
    # This function verifies if the next sublist has k nodes to reverse it
    def isValidList(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    # This is the main function to solve the problem
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First, we create a dummy node, pointing to the original head,
        # and this node acts like our groupPrev pointer
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy

        # The loop has only True as condition because the loop stops 
        # when a sublist has fewer than k nodes
        while True:
            # First, we check if the next sublist has k nodes.
            # If the cublist has k nodes, continue, else, break the loop
            kth = self.isValidList(groupPrev, k)
            if not kth: break

            # Then, we store the next group,
            # Set the previous pointer to the next group,
            # and set the current pointer to the head of the current sublist
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next

            # Reverse the list
            self.reverseList(groupNext, curr, prev)

            # Finally, we connect the tail of the current sublist to the next sublist,
            # and move forward to the next sublist
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
        



        