# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = res_head = ListNode(0)
        carry = False
        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            carry = curr_sum >= 10
            res.val = curr_sum if not carry else curr_sum % 10
            res.next = ListNode(0) if l1.next or l2.next or carry else None
            l1 = l1.next
            l2 = l2.next
            res = res.next

        remaining_list = l1 or l2

        if remaining_list:
            while remaining_list:
                curr_sum = remaining_list.val + carry
                carry = curr_sum >= 10
                res.val = curr_sum if not carry else curr_sum % 10
                res.next = ListNode(0) if remaining_list.next or carry else None
                remaining_list = remaining_list.next
                res = res.next

        if res: 
            res.val = int(carry)

        return res_head
        
        

        

        
