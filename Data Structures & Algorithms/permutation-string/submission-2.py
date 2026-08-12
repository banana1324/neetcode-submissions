class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l2< l1:
            return False
        if s2 == s1:
            return True

        og = {}
        for char in s1:
            og[char] = og.get(char, 0) + 1

        left = 0
        right = 0
        freq = {}
        while right - left < l1:
            freq[s2[right]] = freq.get(s2[right],0) + 1
            right += 1

        while right < l2:


            if og != freq:
                freq[s2[left]] -= 1

                if freq[s2[left]] == 0:
                    del freq[s2[left]]

                left += 1
                print (right)
                print (s2[right])
                print (freq)

                freq[s2[right]] = freq.get(s2[right],0) + 1
                right += 1

            else:
                return True
        if og == freq:
            return True
        return False
