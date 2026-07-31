class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        snum = {}
        tnum = {}
        for letter in s:
            snum[letter] = snum.get(letter, 0) + 1
        for letter in t:
            tnum[letter] = tnum.get(letter, 0) + 1
        if snum == tnum:
            return True
        return False