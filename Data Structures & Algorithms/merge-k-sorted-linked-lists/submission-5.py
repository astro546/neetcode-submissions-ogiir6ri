# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        curr_nodes = []
        dummy = ListNode()
        curr = dummy

        i = 0
        for curr_list in lists:
            curr_node = curr_list
            while curr_node:
                heappush(curr_nodes, (curr_node.val, i, curr_node))
                curr_node = curr_node.next
                i += 1
            
        while curr_nodes:
            _, idx, curr.next = heappop(curr_nodes)
            curr = curr.next
        curr.next = None
        return dummy.next
        