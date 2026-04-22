"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Time: O(n), Space: O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First, if the original linked list is empty, there's nothing to do
        # so, return None
        if head is None: return None

        # First, we do the first pass to create the node hash.
        # The node hash has the following structure:
        # &original node : new Node
        # the & means that is a pointer of the original node
        node = head
        nodes_hash = {}
        while node:
            nodes_hash[node] = Node(node.val)
            node = node.next

        # Then, we do another pass to the original linked list to link random pointers
        node = head
        new_node = nodes_hash[head]
        while node:
            new_node.next = nodes_hash.get(node.next)
            new_node.random = nodes_hash.get(node.random)
            node = node.next
            new_node = new_node.next
        
        return nodes_hash[head]

        