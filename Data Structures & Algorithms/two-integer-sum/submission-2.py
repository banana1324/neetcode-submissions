class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        index = {}
        ans = []
        for x in range(0, len(nums)):
            diff[target - nums[x]] = x
            index[nums[x]] = x
        for x in range(0, len(nums)):
            if nums[x] in diff and x != diff[nums[x]]:
                ans =[min(x, diff[nums[x]]), max(x, diff[nums[x]])]
                return ans