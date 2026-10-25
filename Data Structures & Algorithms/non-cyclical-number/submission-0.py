class Solution:
    def isHappy(self, n: int) -> bool:
        
        while True:
            length = len(str(n))
            summ = 0
            for _ in range(length):
                summ += (n % 10) ** 2
                n = n // 10
                
            if summ == 4:
                return False
            if summ == 1:
                return True
            n = summ