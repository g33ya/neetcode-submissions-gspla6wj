# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        
        if not a or not b:
            return False
        
        left_same = self.isSameTree(a.left, b.left)
        right_same = self.isSameTree(a.right, b.right)
        
        return a.val == b.val and left_same and right_same
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        matches_here = self.isSameTree(root, subRoot)
        matches_left = self.isSubtree(root.left, subRoot)
        matches_right = self.isSubtree(root.right, subRoot)

        return matches_here or matches_left or matches_right

    

            
