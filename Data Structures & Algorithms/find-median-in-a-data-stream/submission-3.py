class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums= sorted(self.nums)
        if len(self.nums) == 1:
            return self.nums[0]

        if len(self.nums) == 2:
            return (self.nums[0] + self.nums[1]) /2

        if len(self.nums) % 2 ==0 :

            return ((self.nums[len(self.nums)//2-1] + self.nums[len(self.nums)//2] )/2)

        else: return self.nums[len(self.nums) //2]