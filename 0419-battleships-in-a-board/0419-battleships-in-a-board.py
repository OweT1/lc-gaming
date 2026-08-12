class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n_rows, n_cols = len(board), len(board[0])

        visited = [[0]*n_cols for _ in range(n_rows)]

        res = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == 'X' and not visited[r][c]:
                    queue = [(r, c)]
                    while queue:
                        t_r, t_c = queue.pop()
                        for direction in DIRECTIONS:
                            new_r, new_c = t_r + direction[0], t_c + direction[1]
                            if (
                                new_r >= 0 and
                                new_r < n_rows and
                                new_c >= 0 and
                                new_c < n_cols and
                                not visited[new_r][new_c] and
                                board[new_r][new_c] == 'X'
                            ):
                                queue.append((new_r, new_c))
                                visited[new_r][new_c] = 1
                    res += 1
        return res



        