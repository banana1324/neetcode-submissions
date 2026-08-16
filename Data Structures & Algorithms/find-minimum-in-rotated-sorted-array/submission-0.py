class Solution:
    def findMin(self, nums: List[int]) -> int:
        small = nums[0]
        for num in nums:
            if num < small:
                small = num

        return small