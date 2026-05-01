# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n), Space: O(n)
    # We use recursive DFS in this solution
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # In each node, we check if the node is inside of the current boundaries,
        # if not, return False.
        # In each calls, we update the boundaries respectively
        def dfs(node, min_limit, max_limit):
            if node is None: return True
            if not(min_limit < node.val < max_limit): return False
            left = dfs(node.left, min_limit, node.val)
            right = dfs(node.right, node.val, max_limit)
            return left and right

        return dfs(root, float('-inf'), float('inf'))
        