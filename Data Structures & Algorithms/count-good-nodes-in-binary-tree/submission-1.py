# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        Information I need: max_val of path before me
        What to do with that: check if my current value is >= the max_val i've seen so far
        I will need to return my max_val to my children
        Empty node should return 0
        '''
        good_count = 0

        def dfs(root, max_val):
            nonlocal good_count
            new_max_val = 0

            if not root:
                return 0
            
            if root.val >= max_val:
                good_count += 1
            
            new_max_val = max(root.val, max_val)

            left = dfs(root.left, new_max_val)
            right = dfs(root.right, new_max_val)

        dfs(root, root.val)
        return good_count
