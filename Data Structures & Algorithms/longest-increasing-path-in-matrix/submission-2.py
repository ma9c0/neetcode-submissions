class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = [[None] * len(matrix[0]) for _ in range(len(matrix))]

        def searcher(x, y):
            nonlocal dp
            
            max_ans = 0
            for x1, y1 in ((x + 1, y), (x, y + 1),
                           (x - 1, y), (x, y - 1)):

                if x1 < 0 or y1 < 0 or x1 == len(matrix) or y1 == len(matrix[0]) \
                    or matrix[x1][y1] <= matrix[x][y]:
                    continue

                if dp[x1][y1] is None:
                    searcher(x1, y1)

                max_ans = max(max_ans, dp[x1][y1])
            dp[x][y] = max_ans + 1

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):

                if dp[x][y] is None:
                    searcher(x, y)

        return max(max(line) for line in dp)