class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #lets do some bubble sorting
        leng = len(nums)
        if leng == 1: return

        currLeng = leng
        for x in range(leng):
            l = 0
            r = 1
            for y in range(leng-1):
                if nums[l] > nums[r]:
                    store = nums[l]
                    nums[l] = nums[r]
                    nums[r] = store
                l += 1
                r += 1
            currLeng -= 1
        return