class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binsearch(left, right):
            if left > right:
                return -1
            
            midIndx = (left + right) // 2

            if nums[midIndx] == target:
                return midIndx
            elif nums[midIndx] > target:
                return binsearch(left, midIndx -1)
            else:
                return binsearch(midIndx + 1, right)
        return binsearch(0, len(nums) - 1)