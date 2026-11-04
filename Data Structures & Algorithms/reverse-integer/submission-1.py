class Solution:
    def reverse(self, x: int) -> int:
        #final = 0000000000000000000000000000000
        #begin = f"{x:b}"
        stringg = str(x)
        res = ""
        for x in range(len(stringg)-1, -1, -1):
            res += (stringg[x])
        if res[-1] == "-":
            res = "-" + res[:-1]
        res = int(res)
        if res > 2**31-1 or res < 2**31 * -1:
            return 0
        return res
        
