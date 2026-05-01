# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # Time: O(n), Space: O(n)
    # This solution use BFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            
            # Since we first push the right elements, the first element to exit from the queue
            # is the element that will be visible from the right
            res.append(queue[0].val)
            for _ in range(n):
                node = queue.popleft()
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
        return res