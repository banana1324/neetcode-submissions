class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        ls = len(s)
        lt = len(t)
        if lt > ls:
            return ""

        freqt = {}
        for char in t:
            freqt[char] = freqt.get(char,0) + 1
            if char not in s:
                return ""

        need = len(freqt)

        left = 0
        right = 0
        freqs = {}
        have = 0
       #need = 0 (alr defined up there)
        yeea = ""
        while right < ls:
            if s[right] in t:
                freqs[s[right]] = freqs.get(s[right],0) + 1 
                if freqs[s[right]] == freqt[s[right]]:
                    have += 1
 
            while have == need:
                if yeea == "":
                    yeea = s[left:right + 1]
                    swapped = True
                    
                elif (right - left + 1) < len(yeea):
                    yeea = s[left:right + 1]

                if s[left] in t:
                    freqs[s[left]] -= 1
                    if freqs[s[left]] < freqt[s[left]]:
                        have -= 1
                    if freqs[s[left]] == 0:
                        del freqs[s[left]]
                    
                left += 1
            
            right += 1
        
        return yeea
            
        
