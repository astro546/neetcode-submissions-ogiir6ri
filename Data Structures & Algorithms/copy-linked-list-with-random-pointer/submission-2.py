"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None

        node = head
        nodes_hash = {}
        while node:
            nodes_hash[node] = Node(node.val)
            node = node.next

        node = head
        new_node = nodes_hash[head]
        while node:
            new_node.next = nodes_hash.get(node.next)
            new_node.random = nodes_hash.get(node.random)
            node = node.next
            new_node = new_node.next
        
        return nodes_hash[head]

        