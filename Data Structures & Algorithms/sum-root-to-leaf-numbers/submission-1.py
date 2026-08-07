# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        1. this is a downward traversal. from my parent i'll need to know their concatenation
        2. from here i'll append my value to their concatenation
        3. i'll need to pass down that new concat to my child
        4. final answer is computed by adding together the left concat and right concat
        5. base case empty tree returns 0
        need a helper bc the final step is to compute the sum, from which i'll need the left 
        and right concats
        concats: prev concat * 10 + curr val
        '''
        if not root:
            return 0
        
        def dfs(root, path):
            if not root:
                return 0

            updated_path = path * 10 + root.val

            if not root.left and not root.right:
                print(updated_path)
                return updated_path
            
            left_path = dfs(root.left, updated_path)
            right_path = dfs(root.right, updated_path)
            return left_path + right_path

        return dfs(root, 0)
