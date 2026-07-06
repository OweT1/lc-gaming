class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = []
        row_len, col_len = len(board), len(board[0])
        
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == word[0]:
                    start.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for s in start:
            visited = [[0]*col_len for _ in range(row_len)]
            s_r, s_c = s
            visited[s_r][s_c] = 1

            exists = False
            def check_existence(curr: tuple[int], i: int):
                if i == len(word):
                    nonlocal exists
                    exists = True
                    return
                char_to_find = word[i]
                for d in directions:
                    new_r, new_c = curr[0] + d[0], curr[1] + d[1]
                    if (
                        (new_r >= 0 and new_r < row_len) and \
                        (new_c >= 0 and new_c < col_len) and \
                        board[new_r][new_c] == char_to_find and \
                        not visited[new_r][new_c] \
                    ):
                        visited[new_r][new_c] = 1
                        check_existence((new_r, new_c), i+1)
                        visited[new_r][new_c] = 0
            check_existence(s, 1)
            if exists:
                return True
        return False

