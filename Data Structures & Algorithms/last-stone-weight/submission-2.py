class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        while len(stones) >= 2:
            stones = sorted(stones)
            heavy1 = stones.pop()
            heavy2 = stones.pop()
            if heavy1 - heavy2 > 0:
                stones.append(heavy1 - heavy2)
        
        if len(stones) == 1:
            return stones[0]
        if not stones:
            return 0
        return stones[1] - stones[0]
