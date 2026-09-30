class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroes = [(r, c) for r in range(m) for c in range(n) if matrix[r][c] == 0]

        for r, c in zeroes:
            for i in range(n):
                matrix[r][i] = 0
            for j in range(m):
                matrix[j][c] = 0        