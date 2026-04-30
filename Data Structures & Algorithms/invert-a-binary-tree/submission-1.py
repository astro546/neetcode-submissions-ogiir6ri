# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n), Space: O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # We perform a DFS to invert the tree, in which call, we return a new node
        # with their sons inverted
        def dfs(root):
            if root is None: return
            left = dfs(root.left)
            right = dfs(root.right)
            return TreeNode(root.val, left=right, right=left)

        return dfs(root)
        