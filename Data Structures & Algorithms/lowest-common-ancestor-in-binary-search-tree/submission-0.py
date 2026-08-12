# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        1. What do I need to know at a node?
            - whether p and q are both in my subtree
        2. What do I do with this information?
            return LCA if they are not
        3. What do I pass down to my children?
            - p and q
        4. How do i get my final answer? 
            - answered by #2
        5. Base case(s)
            - will come back to this .. oops
        '''
        
        if not root:
            return None

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root
        
       
        
      
           

            





