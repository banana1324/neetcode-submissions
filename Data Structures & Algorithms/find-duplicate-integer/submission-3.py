class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #this is gon be pretty slow
        fastnum = nums[0]
        slownum = nums[0]
        slowv2 = nums[0]
        while True:


            slownum = nums[slownum]
            fastnum = nums[nums[fastnum]]


            if slownum == fastnum:
                break
        while True:
            if slowv2 == slownum:
                return slownum
            slownum = nums[slownum]
            slowv2 = nums[slowv2]

            if slowv2 == slownum:
                return slownum