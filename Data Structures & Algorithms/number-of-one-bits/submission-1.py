class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for x in range(32):
            if n & 1<<x == 1<<x:
                res += 1
        return res