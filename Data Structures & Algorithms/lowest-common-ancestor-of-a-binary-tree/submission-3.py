# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        1. What info do I need at this node 
            - if children has subtree containing p and q
        2. What do I do with that information
            - track current LCA, explore further down into the subtree
        3. What do I need to return
            - whether my subtree contains p and q
        4. How is the final answer collected
            - need to update LCA while traversing down
        5. What are my base cases
            - if not root, None. 
        '''
        lca = root

        def dfs(root):
            nonlocal lca
            if not root:
                return None
            
            if not root.left and not root.right:
                return lca

            if root.left and self.subtreeNodes(root.left, p, q):
                lca = root.left
                dfs(root.left)
            elif root.right and self.subtreeNodes(root.right, p, q):
                lca = root.right
                dfs(root.right)
        dfs(root)
            
        return lca
            

    # helper to create list checking subtree nodes
    def subtreeNodes(self, root, p, q) -> bool:
        # dfs traversal
        nodes = []
        def dfs(root):
            if not root:
                return None

            nodes.append(root.val)

            dfs(root.left)
            dfs(root.right)
        
        
        dfs(root)
        print(nodes)
        return p.val in nodes and q.val in nodes


