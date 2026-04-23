# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(max(m,n)), Space: O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # First, we create our head for the output linked list
        # and, we create a boolean that tell us if in the current sum there is a carry
        res = res_head = ListNode(0)
        carry = False

        # Until we reach the end of l1 or l2 or both
        while l1 and l2:
            # We calculate the current sum, and if the sum is >= 10, there is a carry in the sum
            curr_sum = l1.val + l2.val + carry
            carry = curr_sum >= 10

            # Depends on the carry, we put in the value of the current output node,
            # the result of the sum
            res.val = curr_sum if not carry else curr_sum % 10

            # Create the next output node, and move forward in all linked lists
            res.next = ListNode(0) if l1.next or l2.next or carry else None
            l1 = l1.next
            l2 = l2.next
            res = res.next

        # We check if there is a remaining list, and, if this is true,
        # we iterate the remaining list
        remaining_list = l1 or l2
        if remaining_list:
            while remaining_list:
                curr_sum = remaining_list.val + carry
                carry = curr_sum >= 10
                res.val = curr_sum if not carry else curr_sum % 10
                res.next = ListNode(0) if remaining_list.next or carry else None
                remaining_list = remaining_list.next
                res = res.next

        # Finally, we check if there's any carry left.
        # and, if there is, we assing the carry to this last node
        if res: 
            res.val = int(carry)

        return res_head