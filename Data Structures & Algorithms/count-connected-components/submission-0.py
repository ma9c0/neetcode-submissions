class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # connection graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        unvisited = [1] * n
        comp = 0
        def DFS(node, parent):
            
            if unvisited[node] == 0:
                return

            unvisited[node] = 0

            for neighbors in graph[node]:
                if neighbors != parent:
                    DFS(neighbors, node)

        for x, v in enumerate(unvisited):
            if v == 1:
                DFS(x, x)
                comp += 1

        return comp
