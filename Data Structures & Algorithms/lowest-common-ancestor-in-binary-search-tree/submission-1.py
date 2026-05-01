# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(h), Space: O(h), h = height of the tree
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we use a global variable to store the lsa
        self.lca = None

        # We found the lca checking if the current node value is between p and q
        def dfs(node):
            nonlocal p, q
            if node is None: return None
            left = dfs(node.left)
            right = dfs(node.right)
            is_lca = node.val <= max(p.val, q.val) and node.val >= min(p.val, q.val)
            if is_lca: self.lca = node

        dfs(root)
        return self.lca
        