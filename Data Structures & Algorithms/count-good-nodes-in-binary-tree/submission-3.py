# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Time: O(n), Space: O(n)
        # This solution uses recursive DFS
        # In each node, we update the max number until we reach the current node.
        # If the current node is >= than the current max number, this is a good node
        def dfs(node, curr_maxNum):
            if node is None: return 0
            maxNum = max(curr_maxNum, node.val)
            res = 1 if maxNum == node.val else 0
            res += dfs(node.left, maxNum)
            res += dfs(node.right, maxNum)
            return res
        
        return dfs(root, root.val)