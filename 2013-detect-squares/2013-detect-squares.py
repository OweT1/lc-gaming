class DetectSquares:

    def __init__(self):
        self.x_axis = {}
        self.y_axis = {}
        
    def add(self, point: List[int]) -> None:
        x, y = point
        if x not in self.x_axis:
            self.x_axis[x] = {}
        if y not in self.x_axis[x]:
            self.x_axis[x][y] = 0
        if y not in self.y_axis:
            self.y_axis[y] = {}
        if x not in self.y_axis[y]:
            self.y_axis[y][x] = 0
        self.x_axis[x][y] += 1
        self.y_axis[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        if x not in self.x_axis: return 0

        x_list = self.x_axis[x]
        res = 0
        for new_y, c in x_list.items():
            if new_y == y: continue
            y_change = new_y - y
            dist = abs(y_change)
            res += c * self.x_axis.get(x-dist, {}).get(y, 0) * self.x_axis.get(x-dist, {}).get(new_y, 0)
            res += c * self.x_axis.get(x+dist, {}).get(y, 0) * self.x_axis.get(x+dist, {}).get(new_y, 0)
        return res
            

            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)