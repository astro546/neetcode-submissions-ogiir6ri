# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time: O(n), Space: O(n)
    # This solution use the iterative version of DFS
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]

        # We use a hashmap to map the nodes with its diameter and its height
        # This first pair maps a null node with its diameter and its height
        mp = {None: (0,0)}

        while stack:
            # First, we get the top of the stack
            node = stack[-1]

            # Push their sons if they exists and are not in mp hash
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            
            # Else, if their cons does not exists or are in mp hash
            else:
                # Pop the top element of the stack
                node = stack.pop()

                # Get its left and right height and diameter,
                # When we get a null node for the first time, we also obtain its height and diameter
                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                # update the height and diameter
                # To update the height, due to there's no global variable, we need to compare the current diameter, the left and right diamaters
                mp[node] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]
            