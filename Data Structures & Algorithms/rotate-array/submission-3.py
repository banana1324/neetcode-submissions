class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverseL2R (l,r):
            while l<r:
                store = nums[l]
                nums[l] = nums[r]
                nums[r] = store
                l += 1
                r -= 1

        reverseL2R(0,len(nums) -1)
        reverseL2R(0, (k)% len(nums)-1)
        reverseL2R(k% len(nums), len(nums)-1)

