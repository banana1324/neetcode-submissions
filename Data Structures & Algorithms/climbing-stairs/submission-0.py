class Solution:
    def climbStairs(self, n: int) -> int:
        curr = n - 1
        stepPoss = {n : 1}

        while curr >= 0:
            res = 0
            
            if curr + 1 in stepPoss:
                res += stepPoss[curr + 1]

            if curr + 2 in stepPoss:
                res += stepPoss[curr + 2]  

            stepPoss[curr] = res
            curr -= 1
        return stepPoss[0]
    
            
