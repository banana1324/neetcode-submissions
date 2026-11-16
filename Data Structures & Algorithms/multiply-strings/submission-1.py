class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 =="0" or num2 =="0":
            return "0"
        res1=0
        res2=0

        

        di = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        idk = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 0:"0"}

        for letter in num1:
            res1 *= 10
            res1 += di[letter]
        
        for letter in num2:
            res2 *= 10
            res2 += di[letter]

        out = res1 * res2
        print(out)
        result = ""
        while out >0:
            digit = out % 10
            print(digit)
            result = idk[digit] + result
            out //=10
        return result