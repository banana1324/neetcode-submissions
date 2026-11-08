class NumArray:

    def __init__(self, nums: List[int]):
        self.list = nums

    def sumRange(self, left: int, right: int) -> int:
        tot = 0
        for x in range(left, right + 1):
            tot += self.list[x]
        return tot


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)