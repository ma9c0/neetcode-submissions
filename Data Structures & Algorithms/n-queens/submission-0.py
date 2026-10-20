from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diagonals = set()       # row - col
        anti_diagonals = set()  # row + col

        def backtrack(row: int) -> None:
            if row == n:
                result.append(["".join(board_row) for board_row in board])
                return

            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col

                if (
                    col in cols
                    or diagonal in diagonals
                    or anti_diagonal in anti_diagonals
                ):
                    continue

                # Choose this position
                board[row][col] = "Q"
                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)

                backtrack(row + 1)

                # Undo the choice
                board[row][col] = "."
                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)

        backtrack(0)
        return result
