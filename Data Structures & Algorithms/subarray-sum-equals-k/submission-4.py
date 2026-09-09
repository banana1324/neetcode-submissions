class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefSum = {0:1}
        currSum = 0
        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefSum.get(diff,0)
            prefSum[currSum] = prefSum.get(currSum, 0) + 1
        return res