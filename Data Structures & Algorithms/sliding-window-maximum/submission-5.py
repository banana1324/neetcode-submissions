class Solution:
    import heapq
    #O(nlogn) time, using a slidingwindow/heap technique
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        leng = len(nums)
        res = [] #results
        heap = [] #store-er


        for r in range(leng):
            heapq.heappush(heap, (-nums[r], r))

            #currindex - substringleng = last thing outside of substring (4-3 = 0, index 0 is out) 
            while heap[0][1] <= r-k: 
                heapq.heappop(heap) #removes out number
            
            #now the first one will be the biggest and inside the valid substring
            if r >= k-1: #wont append if the window hasn't reached k length
                res.append(-heap[0][0])
            
        
            

        return res
