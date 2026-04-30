# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        def dfs(root, curr_height):
            if root is None: return curr_height
            left = dfs(root.left, curr_height+1)
            right = dfs(root.right, curr_height+1)
            return max(left, right)

        return dfs(root, 0)
        