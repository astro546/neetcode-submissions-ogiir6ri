# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, curr_maxNum):
            if node is None: return
            maxNum = max(curr_maxNum, node.val)
            if maxNum == node.val: self.res += 1
            dfs(node.left, maxNum)
            dfs(node.right, maxNum)
        
        dfs(root, -100)
        return self.res