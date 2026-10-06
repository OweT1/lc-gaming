class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        start, end = min(e[0] for e in events), max([e[1] for e in events])
        events.sort()
        heap = []
        res, j = 0, 0

        for t in range(start, end+1):
            # ingest available events
            while j < len(events) and events[j][0] <= t:
                heapq.heappush(heap, events[j][1])
                j += 1

            # remove events that are over due
            while heap and heap[0] < t:
                heapq.heappop(heap)
            
            # if there are still remaining events, we take the event that ends the earliest
            if heap:
                heapq.heappop(heap)
                res += 1

        return res
