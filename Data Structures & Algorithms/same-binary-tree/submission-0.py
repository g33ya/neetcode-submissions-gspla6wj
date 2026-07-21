# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        cases:
            - both nodes null: return true (base case)
            - one node null: return false (not equal)
            - both nodes not null: 3 things need to match:
                - left subtrees of p and q are equal
                - right substrees of p and q are equal
                - values of p and q are equal
        '''
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same and p.val == q.val