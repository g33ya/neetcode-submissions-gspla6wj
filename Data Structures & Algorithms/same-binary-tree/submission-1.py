# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Recursive DFS
        - 1. promise: returns whether or not two trees are equivalent
        - 2. base case: if not node return True (made it to end),
            if p.val != q.val return False (not equal)
        - 3. assume left/right subtrees are solved. how do i return final
        answer? p.val == q.val and left equal and right equal
        '''

        if not p and not q:
            return True
        
        if not p or not q:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return p.val == q.val and left_same and right_same