# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(n), Space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We use two pointers:
        # f (fast): This pointer advances 2 by 2 nodes
        # s (slow): This pointer advances 1 by 1 nodes
        # If the linked list has a cycle, in some moment, both pointers are going to meet
        f = s = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s:
                return True
        return False
        