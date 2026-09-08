class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        x =0 
        for x in range(len(prices) -1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum