class Solution:
    def generate(self, numRows: int) -> list[list[int]]:       
        res = [[1]]
        for i in range(1, numRows):
            prev, temp = res[-1], []
            for j in range(i+1): # elements
                if j == 0 or j == i: temp.append(1)
                else:
                    temp.append(prev[j-1] + prev[j])
            res.append(temp.copy())
        return res