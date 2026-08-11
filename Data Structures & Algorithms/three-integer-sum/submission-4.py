class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        leng = len(nums)
        res = []

        for x in range(leng):
            l = x + 1
            r = leng - 1
            targ = -nums[x]

            # duplicate x
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            while l < r:
                if nums[l] + nums[r] == targ:
                    res.append([nums[x], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # skip duplicate l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # skip duplicate r
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[l] + nums[r] > targ:
                    r -= 1

                else:
                    l += 1

        return res