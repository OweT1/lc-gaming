class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        rows, cols = len(matrix), len(matrix[0])
        visited = [[False]*cols for _ in range(rows)]
        directions_map = {
            0: (0, 1),
            1: (-1, 0),
            2: (0, -1),
            3: (1, 0)
        }

        direction = 0
        res = []
        curr = (0, 0)

        def validate_position(i: int, j: int) -> bool:
            if (
                i >= 0 and
                i < rows and
                j >= 0 and
                j < cols and
                not visited[i][j]
            ):
                return True
            return False

        while not all([flag for sublist in visited for flag in sublist]):
            i, j = curr
            res.append(matrix[i][j])
            visited[i][j] = True

            # Find new curr
            dir_count = 4
            while dir_count > 0:
                add_i, add_j = directions_map[direction]
                new_i, new_j = i + add_i, j + add_j
                if validate_position(new_i, new_j):
                    curr = (new_i, new_j)
                    break
                else:
                    direction = (direction + 1) % 4
                    dir_count -= 1

            if dir_count == 0: break
        return res

    

