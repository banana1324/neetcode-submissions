class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = []
        total = 0
        for x in range(len(nums)):
            total += nums[x]
            self.presum.append(total)
        print(self.presum)
    
            



    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.presum[right]
        else:
            return self.presum[right] - self.presum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)