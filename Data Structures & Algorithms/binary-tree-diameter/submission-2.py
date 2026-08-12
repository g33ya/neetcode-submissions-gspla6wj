# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        will need to return max height of my subtree (so we'll need a helper)
        track max diameter outside
        '''

        max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            nonlocal max_diameter
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            max_diameter = max(max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        return max_diameter