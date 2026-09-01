class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for x, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, x + 1]
            seen[num] = x
        return []
