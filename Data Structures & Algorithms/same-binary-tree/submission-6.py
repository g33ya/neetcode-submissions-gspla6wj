# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        at a single node, need to check if p.val == q.val
        then we need to confirm its subtrees all check out
        '''
        if not q and not p:
            return True
        
        if not q or not p:
            return False
            
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return p.val == q.val and left_same and right_same 