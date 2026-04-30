# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n), Space: O(n)
    # This solution use the recursive version of DFS
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def dfs(root, length):
            if root is None: return 0
            left_h = dfs(root.left, length)
            right_h = dfs(root.right, length) 
            # We track and update both heights, because longest path does not include necessarly the root node,
            # It can be between internal nodes or leaf nodes 
            self.max_diameter = max(self.max_diameter, left_h + right_h)
            return 1 + max(left_h, right_h)
        dfs(root, 0)
        return self.max_diameter