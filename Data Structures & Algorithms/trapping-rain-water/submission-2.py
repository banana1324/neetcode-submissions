class Solution:
    def trap(self, height: List[int]) -> int:
        #calc prefix and suffix max for each index
        #then use the min(prefmax, suffmax) - height[i] for each index
        #thats O(3n) = O(n)!!!!!! (not factorial) 
        #holy balls remember this in the future 

        leng = len(height)
        prefmax = [0] * leng
        suffmax = [0] * leng
        fmax = 0
        backmax = 0
        summ = 0

        for x in range(leng):
            prefmax[x] = fmax
            fmax = max(height[x], fmax)
            
            suffmax[leng-1-x] = backmax
            backmax = max(height[leng-1-x], backmax)
        for x in range(leng):
            if min(prefmax[x] , suffmax[x]) - height[x] >=0:
                summ += min(prefmax[x] , suffmax[x]) - height[x]
        return summ

 

        
        

        