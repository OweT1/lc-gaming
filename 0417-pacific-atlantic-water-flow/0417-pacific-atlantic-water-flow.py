class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        if rows == 1 or cols == 1: return [[r, c] for r in range(rows) for c in range(cols)]

        pacific, atlantic = [[False]*cols for _ in range(rows)], [[False]*cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # pacific
        dq = deque()
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific[row][col] = True
                    dq.append((row, col))
                    visited.add((row, col))
        while dq:
            r, c = dq.popleft()
            for add_r, add_c in directions:
                new_r, new_c = r + add_r, c + add_c
                if new_r >= 0 and new_r < rows and \
                    new_c >= 0 and new_c < cols and \
                    heights[new_r][new_c] >= heights[r][c] and \
                    (new_r, new_c) not in visited:
                    pacific[new_r][new_c] = True
                    dq.append((new_r, new_c))
                    visited.add((new_r, new_c))
        
        # atlantic
        dq = deque()
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if row == rows-1 or col == cols-1:
                    atlantic[row][col] = True
                    dq.append((row, col))
                    visited.add((row, col))
        while dq:
            r, c = dq.popleft()
            for add_r, add_c in directions:
                new_r, new_c = r + add_r, c + add_c
                if new_r >= 0 and new_r < rows and \
                    new_c >= 0 and new_c < cols and \
                    heights[new_r][new_c] >= heights[r][c] and \
                    (new_r, new_c) not in visited:
                    atlantic[new_r][new_c] = True
                    dq.append((new_r, new_c))
                    visited.add((new_r, new_c))
                    
        res = []
        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]: res.append([row, col])
        return res