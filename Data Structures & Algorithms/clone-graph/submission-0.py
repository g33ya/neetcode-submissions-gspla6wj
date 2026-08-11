"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Pretend I'm one node.
        1. What information do I need here ? -> my neighbors
        2. What do I do with that information ? -> make copies
        3. What continues? -> my neighbors
        4. How is final answer collected? -> By connecting new copies of neighbors to new nodes
        5. What's my base case? no nodes, return None

        '''

        oldToNew = {}
        def dfs(node):
            if not node:
                return None

            if node in oldToNew:
                return oldToNew[node]
            
            new_node = Node(node.val)
            oldToNew[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            return new_node
        return dfs(node)


            


