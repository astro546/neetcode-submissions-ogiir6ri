# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_maxNum):
            if node is None: return 0
            maxNum = max(curr_maxNum, node.val)
            res = 1 if maxNum == node.val else 0
            res += dfs(node.left, maxNum)
            res += dfs(node.right, maxNum)
            return res
        
        return dfs(root, root.val)