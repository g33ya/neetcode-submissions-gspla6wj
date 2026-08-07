# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Pretend I'm one node.

        1. What information do I need HERE?
        → from left child: best downward path sum
        → from right child: best downward path sum
        → nothing from parent

        2. What do I DO with that information here?
        → calculate the best complete path THROUGH me:
            my value + left contribution + right contribution

        3. What information needs to continue?
        → RETURN upward:
            my value + max(left contribution, right contribution)

            I can only give my parent ONE branch,
            because a path continuing upward can't split.

        4. How is the FINAL answer collected?
        → track max_sum across all nodes
        → compare it against the path going through me

        5. Base case?
        → empty node returns 0
        '''
        max_sum = float("-inf")

        def best_sum(root):
            nonlocal max_sum

            if not root:
                return 0
            
            left_sum = max(best_sum(root.left), 0) # 2
            right_sum = max(best_sum(root.right), 0) # 3
            
            my_sum = root.val + left_sum + right_sum
            max_sum = max(max_sum, my_sum)
           
            return root.val + max(left_sum, right_sum)
        
        best_sum(root)
        return max_sum