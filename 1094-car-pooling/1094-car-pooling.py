class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        exit_pq = []
        curr = 0
        for trip in sorted(trips, key=lambda x: x[1]):
            p, f, t = trip
            while exit_pq and exit_pq[0][0] <= f:
                curr -= heapq.heappop(exit_pq)[1]
            
            curr += p
            if curr > capacity: return False
            heapq.heappush(exit_pq, (t, p))

        return True

        