class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        for x in range(len(nums)):
            if x == len(nums) - k:
                return nums[x]
