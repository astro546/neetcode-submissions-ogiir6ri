# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n), Space: O(n)
    # This solution use the iterative version of DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        stack = [(root, 1)]
        max_height = 0
        while stack:
            node = stack.pop()
            curr_height = node[1]
            max_height = max(max_height, curr_height)
            if node[0].left: stack.append((node[0].left, curr_height + 1))
            if node[0].right: stack.append((node[0].right, curr_height + 1))
        return max_height