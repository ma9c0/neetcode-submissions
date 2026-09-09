class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for x in range(9):
            for y in range(9):
                current = board[x][y]
                if current == '.':
                    continue
                index = 3*(x//3) + (y//3)
                if current in rows[x] or current in cols[y] or current in squares[index]:
                    return False
                rows[x].add(current)
                cols[y].add(current)
                squares[index].add(current)
        return True