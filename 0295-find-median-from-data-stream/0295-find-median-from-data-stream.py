class MedianFinder:

    def __init__(self):
        self.sorted_arr = []

    def addNum(self, num: int) -> None:
        self.sorted_arr.insert(bisect.bisect_right(self.sorted_arr, num), num) # logN

    def findMedian(self) -> float:
        n = len(self.sorted_arr)
        if n % 2:
            return self.sorted_arr[int(n/2)]
        else:
            return (self.sorted_arr[int(n/2)-1] + self.sorted_arr[int(n/2)]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()