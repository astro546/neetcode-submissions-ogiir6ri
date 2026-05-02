# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n), Space: O(h)
    # This solution uses recursive DFS
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kthSmallest = None
        self.count = 0
        def dfs(node):
            # We check also if kthSmallest is not none to avoid innecessary work
            if node is None or self.kthSmallest is not None: return
            
            # First, we check all left branches.
            # This is since the smallest element on the tree is the leftmost bottomost
            # element of the tree
            dfs(node.left)

            # Then update the counter and check if the current node is the kth smallest element
            self.count += 1
            if self.count == k:
                self.kthSmallest = node.val
                return

            # Finally, check for right branches
            dfs(node.right)

        dfs(root)
        return self.kthSmallest
