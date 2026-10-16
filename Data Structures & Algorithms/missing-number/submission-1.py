class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0
        for x in range(len(nums) + 1):
            res ^= x
        
        for num in nums:
            res ^= num
        return res