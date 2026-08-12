# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        will need to check height balance in every subtree
        '''

        def getHeight(root):
            if not root:
                return 0

            left_height = getHeight(root.left)
            right_height = getHeight(root.right)
            return 1 + max(left_height, right_height)
        
        if not root:
            return True

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)

        return abs(getHeight(root.left) - getHeight(root.right)) <= 1 and left_balanced and right_balanced
            
