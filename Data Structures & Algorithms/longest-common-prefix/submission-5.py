class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""
        short = min(len(string) for string in strs)
        length = len(strs)
        currPref = ""
        pref = ""
        ind = 0

        while ind <= short:
            for curr in strs:
                if curr[:ind] != currPref:
                    return pref
            pref = currPref
            ind += 1
            currPref = strs[0][:ind]
        return pref
        
