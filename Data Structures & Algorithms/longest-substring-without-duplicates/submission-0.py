class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        supabig = 0
        leng = len(s)
        if leng == 0:
            return 0
        letters = {}
        left = 0
        right = 0
        while right < leng:
            letters[s[right]] = letters.get(s[right],0) + 1
            while letters[s[right]] > 1:
                letters[s[left]] -=1
                left+=1
            right +=1
            supabig = max(supabig, right - left)
            if (right - left) > supabig:
                print(s[left:right])

            
        return supabig