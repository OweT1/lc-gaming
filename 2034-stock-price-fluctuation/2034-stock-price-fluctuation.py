class StockPrice:

    def __init__(self):
        self.records = {}
        self.latest_timestamp = 0
        self.prices = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.records:
            curr_price = self.records[timestamp]
            pos = bisect.bisect_left(self.prices, (curr_price, timestamp))
            self.prices.pop(pos)

        self.records[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        pos = bisect.bisect_left(self.prices, (price, timestamp))
        self.prices.insert(pos, (price, timestamp))

    def current(self) -> int:
        return self.records[self.latest_timestamp]

    def maximum(self) -> int:
        return self.prices[-1][0]

    def minimum(self) -> int:
        return self.prices[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()