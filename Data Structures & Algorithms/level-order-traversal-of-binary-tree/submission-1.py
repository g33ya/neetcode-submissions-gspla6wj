from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        all_levels = []

        if not root:
            return []

        while queue:
            level_list = []
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                level_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            all_levels.append(level_list)
        return all_levels










