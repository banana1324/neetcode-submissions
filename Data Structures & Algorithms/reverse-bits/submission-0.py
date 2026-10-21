class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for x in range(32):
            if ((n>>x) & 1) == 1:
                res += 2**(31-x)
        return res

        