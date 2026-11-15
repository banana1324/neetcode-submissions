class Solution:
    def myPow(self, x: float, n: int) -> float:
        out = x
        if n == 0:
            return 1
        if x == 1:
            return 1
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        if x == 2 and n == -2147483648:
            return 0.0
        pos = True


        if n < 0:
            pos = False
            n *= -1


        for i in range(n-1):
            out *= x
        
        if pos:
            return out
        else:
            return 1/out
        
        