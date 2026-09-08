class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_q = deque()
        res = []

        for i, num in enumerate(nums):
            # maintaining a monotonic decreasing queue
            while max_q and max_q[-1] < num:
                max_q.pop()
            max_q.append(num)

            # if max num is out of bounds
            if i >= k and max_q[0] == nums[i-k]:
                max_q.popleft()
            
            # add result
            if i >= k-1:
                res.append(max_q[0])
        return res
                