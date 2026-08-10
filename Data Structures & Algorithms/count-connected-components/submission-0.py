class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        connected_components = 0
        
        def bfs(node):
            queue = collections.deque([node])
            
            while queue:
                node = queue.popleft()
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        for node in range(n):
            if node not in visited:
                connected_components += 1
                bfs(node)
                
        return connected_components


