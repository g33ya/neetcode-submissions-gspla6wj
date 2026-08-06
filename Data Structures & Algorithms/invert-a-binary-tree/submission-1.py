# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Promise: Inverts tree and returns root (MODIFY)
        Base Case: 1 tree, if not root return None
        Modifying? Yes, will need to swap children
        Assume left/right subtrees solved
        Return root
        '''

        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)

        return root