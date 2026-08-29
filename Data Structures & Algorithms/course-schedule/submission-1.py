class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        safe = [0] * numCourses
        def DFS(course):
            if safe[course] == 1: 
                return False
            if safe[course] == 2:
                return True
            safe[course] = 1

            for preq in graph[course]:
                if not DFS(preq):
                    return False
            safe[course] = 2
            return True

        for course in range(numCourses):
            if not DFS(course): return False

        return True