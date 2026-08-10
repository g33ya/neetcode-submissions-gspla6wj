class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        # no cycles!

        queue = collections.deque([(0, -1)])
        visited.add(0)
        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                queue.append((neighbor, node))
        return len(visited) == n

      