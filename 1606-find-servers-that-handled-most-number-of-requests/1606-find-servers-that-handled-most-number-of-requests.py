class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        before = list(range(k))
        after = []
        busy = [] # to be flipped
        server_counter = [0]*k

        for i, (arr, ld) in enumerate(zip(arrival, load)):
            server_id = i % k
            if server_id == 0: before, after = [], before

            while busy and busy[0][0] <= arr:
                _, s_id = heapq.heappop(busy)
                if s_id < server_id: heapq.heappush(before, s_id)
                else: heapq.heappush(after, s_id)

            available = after if after else before
            if not available: continue

            to_add = heapq.heappop(available)
            heapq.heappush(busy, (arr+ld, to_add))
            server_counter[to_add] += 1
        max_count = max(server_counter)
        return [i for i, num in enumerate(server_counter) if num == max_count]


