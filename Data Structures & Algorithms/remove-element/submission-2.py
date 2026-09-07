class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leng = len(nums)
        right = 0
        left = 0
        k = 0
        while left < leng:
            if nums[left] == val:
                right = left
                while nums[right] == val and right < leng - 1:
                    right += 1
                store = nums[left]
                nums[left] = nums[right]
                nums[right] = store
            left += 1

        return leng - nums.count(val)

"""
        0 1 2 2 3 0 4 2
        0 1 3 2 2 0 4 2
        0 1 3 0 2 2 4 2
        0 1 3 0 4 2 2 2
"""