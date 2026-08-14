class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return max(points[0])
    
        num_cols = len(points[0])
        prevArr = points[0]

        for r in range(1, len(points)):
            left, right = [], []
            
            for i in range(num_cols):
                if i == 0:
                    left.append(prevArr[i])
                    right.append(prevArr[num_cols-i-1])
                else:
                    left.append(max(prevArr[i], left[i-1]-1))
                    right.append(max(prevArr[num_cols-i-1], right[i-1]-1))

            currArr = []
            right = right[::-1]
            for i in range(num_cols):
                currArr.append(points[r][i] + max(left[i], right[i]))
            prevArr = currArr.copy()
        
        return max(currArr)



