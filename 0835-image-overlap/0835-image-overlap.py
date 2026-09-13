class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        if n == 1: return img1[0][0] and img2[0][0]

        ones = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        res = {}
        for row in range(n):
            for col in range(n):
                if img1[row][col] == 1:
                    for one in ones:
                        new_row, new_col = one
                        shift_row, shift_col = new_row - row, new_col - col
                        res[(shift_row, shift_col)] = res.get((shift_row, shift_col), 0) + 1
        return max(res.values()) if res else 0