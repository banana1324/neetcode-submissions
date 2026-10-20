class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        minCost = { n: 0,  n - 1: cost[n - 1]}

        i = n-2

        while i >= 0:
            minCost[i] = cost[i] + min(minCost[i + 1], minCost[i + 2])
            i -=1
        return min(minCost[0], minCost[1])

