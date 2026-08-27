class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)

        beeg = arr[-1]
        
        
        for x in range(l-1, -1,-1):
            curr = arr[x]
            arr[x] = beeg
            beeg = max(curr, beeg)
        arr[-1] = -1
        return arr