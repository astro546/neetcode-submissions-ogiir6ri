# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lca = None
        def dfs(node):
            nonlocal p, q
            if node is None: return None
            left = dfs(node.left)
            right = dfs(node.right)
            is_lca = node.val <= max(p.val, q.val) and node.val >= min(p.val, q.val)
            if is_lca: self.lca = node

        dfs(root)
        return self.lca
        