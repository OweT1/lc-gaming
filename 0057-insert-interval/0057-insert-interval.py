class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        pos = bisect.bisect_right(intervals, newInterval)
        new_intervals = [newInterval] + intervals.copy() if pos == 0 \
                        else [intervals[pos-1]] + [newInterval] + intervals[pos:]

        result = []
        for interval in new_intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result if pos == 0 else intervals[:pos-1] + result
