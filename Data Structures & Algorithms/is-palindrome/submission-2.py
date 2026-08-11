class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        if len(s) == 1 or len(s) == 0:
            return True

        while a<b:
            if not s[a].isalnum():
                a += 1
                continue
            if not s[b].isalnum():
                b -= 1
                continue
            
            if s[a].lower() != s[b].lower():
                return False

            a+=1
            b-=1

        return True


            

            
                