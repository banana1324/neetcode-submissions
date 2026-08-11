class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leng = len(prices)
        big = 0
        for x in range(leng):
            big = max(big, max(prices[x:]) - prices[x])

        return big