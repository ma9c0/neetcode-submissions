class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # lets do a bfs and see if we will get to a visited node from another way
        
        # connection/neighbor graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        
        # bfs to all neighbors of a node
        parents = [-1] * (n)
        def bfs(parent, node):
            # end condition

            if parents[node] != -1:
                return False

            parents[node] = parent

            for neighbors in graph[node]:
                if neighbors == parent:
                    continue
                if not bfs(node, neighbors):
                    return False
            return True

        if not bfs(-1, 0):
            return False

        if -1 in parents[1:]:
            return False

        return True

            