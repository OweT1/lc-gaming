class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        connected = set()
        def dfs(i: int, j: int):
            if board[i][j] == 'O':
                connected.add((i, j))
                board[i][j] = 'X'
                for add_i, add_j in directions:
                    new_i, new_j = i + add_i, j + add_j
                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and board[new_i][new_j] == 'O':
                        dfs(new_i, new_j)
        
        edge_nodes = [(0, i) for i in range(n)] + [(m-1, i) for i in range(n)] + [(i, 0) for i in range(m)] + [(i, n-1) for i in range(m)]

        for i, j in edge_nodes:
            dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if (i, j) in connected else 'X'
        