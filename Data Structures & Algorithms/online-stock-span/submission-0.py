class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        dist = 0
        for x in range(len(self.prices) - 1, -1, -1):
            if self.prices[x] > price:
                self.prices.append(price)
                return dist + 1
            else:
                dist += 1
        self.prices.append(price)
        return dist + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)