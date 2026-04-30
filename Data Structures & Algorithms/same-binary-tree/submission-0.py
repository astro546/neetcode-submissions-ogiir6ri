# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkSameTree(node_p, node_q):
            if not node_p and not node_q: return True
            if not node_p or not node_q: return False
            if node_p.val != node_q.val: return False
            return checkSameTree(node_p.left, node_q.left) and checkSameTree(node_p.right, node_q.right)

        def dfs(node_p, node_q):
            if (node_p is None) ^ (node_q is None): return False
            if node_p is None and node_q is None: return True
            left = dfs(node_p.left, node_q.left)
            right = dfs(node_p.right, node_q.right)
            is_sameTree = checkSameTree(node_p, node_q)
            return is_sameTree and left and right
        
        return dfs(p, q)


        