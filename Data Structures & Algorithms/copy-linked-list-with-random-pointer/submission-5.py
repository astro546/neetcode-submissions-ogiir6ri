"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    # Time: O(n), Space: O(n)
    # This solution execute only one pass to the linked list
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First, we define a hash map that returns a new Node with value of 0 if the key not exists
        node_hash = defaultdict(lambda: Node(0))
        #Then, we declare a None key with none value.
        # This will help us to edge cases
        node_hash[None] = None

        # We execute only one pass, because we first create new nodes with default values for random pointers
        # after or before pointing these nodes by a random pointers, we assign their actual values
        node = head
        while node:
            node_hash[node].val = node.val
            node_hash[node].random = node_hash[node.random]
            node_hash[node].next = node_hash[node.next]
            node = node.next

        return node_hash[head]

        