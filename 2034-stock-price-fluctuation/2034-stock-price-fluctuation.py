class StockPrice:

    def __init__(self):
        self.records = {}
        self.latest_timestamp = 0
        self.min_prices = []
        self.max_prices = []

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        
        heapq.heappush(self.min_prices, (price, timestamp))
        heapq.heappush(self.max_prices, (-price, timestamp))

    def current(self) -> int:
        return self.records[self.latest_timestamp]

    def maximum(self) -> int:
        price, timestamp = heapq.heappop(self.max_prices)
        updated_price = self.records[timestamp]
        
        while -price != updated_price:
            price, timestamp = heapq.heappop(self.max_prices)
            updated_price = self.records[timestamp]
        
        heapq.heappush(self.max_prices, (price, timestamp))
        return -price

    def minimum(self) -> int:
        price, timestamp = heapq.heappop(self.min_prices)
        updated_price = self.records[timestamp]
        
        while price != updated_price:
            price, timestamp = heapq.heappop(self.min_prices)
            updated_price = self.records[timestamp]

        heapq.heappush(self.min_prices, (price, timestamp))
        return price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()