class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct the connecting graph
        graph = [[] for _ in range(numCourses)]
        for preq in prerequisites:
            graph[preq[0]].append(preq[1])

        visited = [0] * numCourses
        res = []

        def DFS(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] = 1
            for preq in graph[course]:
                if not DFS(preq):
                    return False
            visited[course] = 2
            res.append(course)
            return True

        for course in range(numCourses):
            if not DFS(course):
                return []

        return res