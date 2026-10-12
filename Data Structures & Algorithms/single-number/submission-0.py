class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        listt = {}

        for num in nums:
            listt[num] = listt.get(num, 0) + 1
        
        for num in nums:
            if listt[num] == 1:
                return num