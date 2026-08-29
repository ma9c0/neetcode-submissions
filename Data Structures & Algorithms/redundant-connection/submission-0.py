class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]

        def find(x):
            if parents[x] == x:
                return x
            root = find(parents[x])
            parents[x] = root
            return root

        def union(x, y):
            root1, root2 = find(x), find(y)
            parents[root1] = root2
        

        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            else:
                union(edge[0], edge[1])

        # return res
