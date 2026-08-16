class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        before = list(range(k)) # will reverse on first call
        after = []
        busy = []
        server_requests = [0]*k

        for i, arr in enumerate(arrival):
            server_id = i % k
            if server_id == 0:
                after = before
                before = []
    
            # Free busy servers if any
            while busy and busy[0][0] <= arr:
                _, s = heapq.heappop(busy)
                if s < server_id:
                    heapq.heappush(before, s)
                else:
                    heapq.heappush(after, s)
            
            available = after if after else before
            if not available: continue

            new_server = heapq.heappop(available)
            heapq.heappush(busy, (arr + load[i], new_server))
            server_requests[new_server] += 1
        
        max_requests = max(server_requests)
        return [i for i, handled in enumerate(server_requests) if handled == max_requests]
                    