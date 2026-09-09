class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for x in range(len(nums)):
            count[nums[x]] = count.get(nums[x],0) + 1
        for key in count:
            if count[key] > (len(nums) //3):
                res.append(key)
        return res