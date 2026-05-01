# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubroot(node_r, node_sub):
            if node_r is None and node_sub is None: return True
            if node_r is None or node_sub is None: return False
            left = isSubroot(node_r.left, node_sub.left)
            right = isSubroot(node_r.right, node_sub.right)
            return node_r.val == node_sub.val and left and right
            
        def dfs(root):
            nonlocal subRoot
            if root is None and subRoot is None: return True
            if root is None or subRoot is None: return False
            is_subroot = isSubroot(root, subRoot)
            left = dfs(root.left)
            right = dfs(root.right)
            return is_subroot or left or right

        return dfs(root)

        