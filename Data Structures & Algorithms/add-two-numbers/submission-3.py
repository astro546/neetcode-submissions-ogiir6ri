# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(max(m,n)), Space: O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # In this solution, we use a dummy node to create the output linked list
        dummy = ListNode()
        cur = dummy
        carry = 0

        # Also, we use an only while loop.
        # We execute this loop until there's no l1 and l2 nodes and no carry
        while l1 or l2 or carry:
            # Get the values of each linked list
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate the current sum
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # Move formard in all linked lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy.next

