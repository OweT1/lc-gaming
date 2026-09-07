class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        colour_counter = Counter(nums)
        red = colour_counter.get(0, 0)
        white = colour_counter.get(1, 0) + red
        blue = colour_counter.get(2, 0) + white

        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < white:
                nums[i] = 1
            else:
                nums[i] = 2

    
        