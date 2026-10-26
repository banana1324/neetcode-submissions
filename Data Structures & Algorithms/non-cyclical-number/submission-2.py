class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            length = len(str(n))
            summ = 0
            for _ in range(length):
                summ += (n % 10) ** 2
                n = n // 10
            n = summ
            if summ in seen:
                return False
            if summ == 1:
                return True
        
            seen.add(summ)