class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount = {}
        for x in range (0, len(nums)):
            numcount[nums[x]] = numcount.get(nums[x], 0) + 1
       
        ans = []

        for x in range(0, k):
            max_value = max(numcount.values())
            
            for key in numcount:
                if numcount[key] == max_value:
                   
                    ans.append(key)
                    numcount[key] = -1
                    break 
        
        
        return ans
