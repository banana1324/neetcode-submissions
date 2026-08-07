from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for string in strs:
            mapping[tuple(sorted(string))].append(string)

        return list(mapping.values())