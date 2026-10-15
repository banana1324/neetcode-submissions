class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for x in range(n + 1):
            curr = 0
            for y in range(32):
                if x & 1<<y == 1<<y:
                    curr +=1
            res.append(curr)
        return res