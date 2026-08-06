# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Promise: Return whether trees are equivalent (information)
        Base Cases: two trees, need to check if both null or one null
        Modifying tree? No
        Assume left/right subtrees solved
        Return combination
        '''

        if not p and not q:
            return True
        
        if not p or not q:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return p.val == q.val and left_same and right_same