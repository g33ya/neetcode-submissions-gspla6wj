# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        1. what info do i need at one node
            - whether or not my childrens trees have been the same
        2. what do i do with that information
            - combine it with whether or not i'm the same
        3. what do i return up
            - whether im the same tree (p.val == q.val)
        4. combine results
            - p.val == q.val and left_same and right_same
        5. base case(s): if not p or not q, true, if not p or not q, false
        '''
        if not p and not q:
            return True

        if not p or not q:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return p.val == q.val and left_same and right_same
