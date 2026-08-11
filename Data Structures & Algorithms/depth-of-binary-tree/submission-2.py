# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        i'm at THIS NODE
        1. what information do i need (INFO!)
            - the depth of my childrens subtrees)
        2. what do i do with that information:
            - add one to the max depth between the two
        3. what do i pass up:
            - my max depth
        4. final answer collected by taking max of left/right
        5. base case : not node returns 0
        '''
        if not root:
            return 0 

        left_child = self.maxDepth(root.left)
        right_child = self.maxDepth(root.right)

        return 1 + max(left_child, right_child)


