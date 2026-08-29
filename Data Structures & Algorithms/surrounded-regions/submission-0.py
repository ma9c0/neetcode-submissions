class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # we do dfs for every O on the border, and replace O with X if 
        # they are not reached by the search. 
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if x == 0 or x == len(board[0]) - 1 or y == 0 or y == len(board) - 1:
                    # do DFS and switch all reachable O to #
                    def DFS(x, y):
                        if x == -1 or x >= len(board[0]) or y == -1 or y >= len(board):
                            return

                        if board[y][x] == '#' or board[y][x] == 'X':
                            return 
                        if board[y][x] == 'O':
                            board[y][x] = '#'
                        
                        DFS(x - 1, y)
                        DFS(x + 1, y)
                        DFS(x, y - 1)
                        DFS(x, y + 1)

                    DFS(x,y)
                        

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == '#':
                    board[y][x] = 'O'
                elif board[y][x] == 'O':
                    board[y][x] = 'X'
        