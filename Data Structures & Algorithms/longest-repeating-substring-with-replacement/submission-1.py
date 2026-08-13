class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        leng = len(s)
        left = 0
        right = 0
        biggest = 0
        if leng == 0:
            return 0
        freq = {}
        newk = k
        while right < leng:
            freq[s[right]] = freq.get(s[right], 0) + 1

            while ((right - left) + 1 ) - max(freq.values()) > k:

                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
                
            biggest = max(right-left + 1, biggest)
            right += 1
        
        return biggest