class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)

        for x in range(l):
            nums.append(0)

        for x in range(l):
            nums[x + l] = nums[x]

        return nums