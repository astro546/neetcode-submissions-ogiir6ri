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
        stack = [root]
        curr = root
        index = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            index += 1
            if index == k:
                return curr.val

            curr = curr.right
