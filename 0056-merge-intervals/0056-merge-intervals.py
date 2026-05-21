class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        ## Requires additional memory
        # output = []
        # for interval in intervals:
        #     if not output or interval[0] > output[-1][1]:
        #         output.append(interval)
        #     else:
        #         output[-1][1] = max(output[-1][1], interval[1])

        ## Modifies the list, but incurs O(n) popping cost
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1
        return intervals
        