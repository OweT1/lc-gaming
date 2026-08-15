class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        s_meetings = sorted(meetings, key = lambda x: x[0])
        free, busy = [], []
        room_counter = [0]*n
        
        # Initialise free meeting rooms - free rooms only have id but busy rooms will be prioritised by time first
        for i in range(n):
            heapq.heappush(free, i)
    
        for start, end in s_meetings:
            # We will reset some of the rooms that end before the room_end
            while busy:
                b_room = heapq.heappop(busy)
                if b_room[0] <= start:
                    heapq.heappush(free, b_room[1])
                else:
                    heapq.heappush(busy, b_room)
                    break

            # Take from free meeting rooms
            if free:
                f_room = heapq.heappop(free)
                heapq.heappush(busy, (end, f_room))
                room_counter[f_room] += 1
        
             # If no free meeting rooms, check busy rooms to get the first starting - as we will already process busy rooms to those that are free, we will simply add based on when the room is free
            else:
                room_end, room = heapq.heappop(busy)
                heapq.heappush(busy, (room_end + end - start, room))
                room_counter[room] += 1

        max_room_booking = max(room_counter)
        for i, c in enumerate(room_counter):
            if c == max_room_booking:
                return i
                
                    



            



        