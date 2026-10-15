class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aten = 0
        bten = 0

        po = 0
        for x in range(len(a) - 1, -1, -1):
            if a[x] == "1":
                aten += 2**po
            po += 1
        po =0 
        for x in range(len(b) - 1, -1, -1):
            if b[x] == "1":
                bten += 2**po
            po += 1
        
        aten += bten

        res = ""
        print(aten)
        while aten >= 1:
            print(aten)
            res = str(aten % 2) + res
            aten //= 2
        if res == "":
            return "0"
        return res