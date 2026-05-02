# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n), Space: O(h)
    # This solution uses iterative DFS
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Instead of adding in a index, we decrement k until k will be 0
            # if k = 0, we already found the kth smallest element
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right
