# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time; O(n log n), space: O(n)
from heapq import heappush, heappop
class Solution:    
    # This solutions iterates by all nodes of all lists in the lists array,
    # and push them into a min heap.
    # Finally, creates the output linked list by popping the nodes from the min heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        curr_nodes = []
        dummy = ListNode()
        curr = dummy

        i = 0
        for curr_list in lists:
            curr_node = curr_list
            while curr_node:
                # We use the value like the main factor to sort the heap,
                # and i like an global index like the second factor to sort the heap
                heappush(curr_nodes, (curr_node.val, i, curr_node))
                curr_node = curr_node.next
                i += 1
            
        while curr_nodes:
            _, idx, curr.next = heappop(curr_nodes)
            curr = curr.next
        curr.next = None
        return dummy.next
        