# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        first we need to find where root.val == subRoot.val, then we need to return if
        those trees are the same.
        '''

        def isSame(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            left_same = isSame(p.left, q.left)
            right_same = isSame(p.right, q.right)

            return p.val == q.val and left_same and right_same

        if not root:
            return False
        
        left_subtree = self.isSubtree(root.left, subRoot)
        right_subtree = self.isSubtree(root.right, subRoot)
        return root.val == subRoot.val and isSame(root, subRoot) or left_subtree or right_subtree
            
