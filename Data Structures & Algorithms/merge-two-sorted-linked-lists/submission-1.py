# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # First, we create an auxiliary node at the start of the new liked list
        # Also, create a node variable to track the current node, and it has teh same value as dummy
        dummy = node = ListNode()

        # Until we reach the end of list1 or list2
        while list1 and list2:
            # If the current value of list2 is less than the current value of list1,
            # Link the current node of the output linked list to list2,
            # And move the pointer in list2.
            if list2.val <= list1.val:
                node.next = list2
                list2 = list2.next
            # Else, do the same in list1
            else:
                node.next = list1
                list1 = list1.next
            # Move the pointer in the output array
            node = node.next

        # If we reach the end of one list, but if another list has remaining nodes,
        # point the current node to that list
        node.next = list1 or list2

        # dummy.next is the head of the output linked list
        return dummy.next