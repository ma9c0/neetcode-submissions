class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        seen = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        def dfs(node_row, node_col):
            if seen[node_row][node_col] != 0:
                return seen[node_row][node_col]
            longest = 1

            for dr, dc in directions:
                next_row = node_row + dr
                next_col = node_col + dc

                if (
                    0 <= next_row < len(matrix)
                    and 0 <= next_col < len(matrix[0])
                    and matrix[next_row][next_col] > matrix[node_row][node_col]
                ):
                    longest = max(
                        longest,
                        1 + dfs(next_row, next_col)
                    )

            seen[node_row][node_col] = longest
            return longest

        answer = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                answer = max(answer, dfs(row, col))

        return answer
