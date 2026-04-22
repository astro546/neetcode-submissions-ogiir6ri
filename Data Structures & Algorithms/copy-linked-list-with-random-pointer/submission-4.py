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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_hash = defaultdict(lambda: Node(0))
        node_hash[None] = None

        node = head
        while node:
            node_hash[node].val = node.val
            node_hash[node].random = node_hash[node.random]
            node_hash[node].next = node_hash[node.next]
            node = node.next

        return node_hash[head]

        