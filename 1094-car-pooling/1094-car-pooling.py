class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for trip in trips:
            p, f, t = trip
            events.append((f, p))
            events.append((t, -p))

        curr = 0
        for e in sorted(events):
            _, p = e
            curr += p
            if curr > capacity:
                return False

        return True

        