class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:    
        pos = bisect.bisect_left(self.bookings, (startTime, endTime))
        if self.bookings and \
            (
                (pos > 0 and startTime < self.bookings[pos-1][1]) or \
                (pos <= len(self.bookings)-1 and endTime > self.bookings[pos][0])
            ):
            return False
        else:
            self.bookings.insert(pos, (startTime, endTime))
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)