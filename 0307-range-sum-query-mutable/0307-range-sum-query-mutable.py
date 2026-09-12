class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.bit = [0]*(self.n+1)
        for i, num in enumerate(nums, 1):
            j = i
            while j <= self.n:
                self.bit[j] += num
                j += j & -j
        

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        index += 1
            
        while index < self.n+1:
            self.bit[index] += delta
            index += index & -index
        
    def query(self, index: int) -> int:
        ans = 0
        while index > 0:
            ans += self.bit[index]
            index -= index & -index
        return ans  
            
    def sumRange(self, left: int, right: int) -> int:
        return self.query(right+1) - self.query(left)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)