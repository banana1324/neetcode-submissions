class Solution:

    def letterfrequency(self,word):
        freq = {}
        for letter in word:
            freq[letter] = freq.get(letter,0) +1
        return freq

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        supercooldictionary = {}
        for word in strs:
            lettfreq = self.letterfrequency(word)
            key = tuple(sorted(lettfreq.items()))
            if key not in supercooldictionary:
                supercooldictionary[key] = []
            
            supercooldictionary[key].append(word)
            ans = []
        for key in supercooldictionary:
            ans.append(supercooldictionary[key])
            
        return ans