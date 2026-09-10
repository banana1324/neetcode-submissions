class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome (string):
            res = ""
            for x in range(len(string) -1,-1,-1):
                res += string[x]
            return res == string
        if isPalindrome(s):
            return True
        for x in range(len(s)):
            delChar = s[:x] + s[x+1:]
            if isPalindrome(delChar):
                return True
        return False