class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs: 
            key = ''.join(sorted(string))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(string)
        dummy = list(hashmap.values())
        return dummy