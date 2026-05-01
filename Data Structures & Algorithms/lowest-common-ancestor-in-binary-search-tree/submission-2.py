# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(h), Space: O(h), h = height of the tree
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr
        