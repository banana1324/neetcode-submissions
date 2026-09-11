class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        ind = 0
        while ind < len(nums) -1:
            if nums[ind + 1] == nums[ind]:
                nums[ind:] = nums[ind+1:]
            else:
                ind += 1
        return len(nums)