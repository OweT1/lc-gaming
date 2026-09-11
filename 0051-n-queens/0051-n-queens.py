class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def isSafe(row: int, col: int) -> bool:
            # col check
            col_check = all([r[col] == '.' for r in board])
            if not col_check: return False

            # diagonals checks
            for i in range(1, min(row, col)+1):
                if board[row-i][col-i] == 'Q': return False
            for i in range(1, min(row, n-1-col)+1):
                if board[row-i][col+i] == 'Q': return False
            return True
    
        def backtrack(row: int):
            if row == n:
                nonlocal res
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    backtrack(row+1)
                    board[row][col] = "."

        backtrack(0)
        return res