import heapq
class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        if len(self.minh) == 0:
            heapq.heappush(self.minh, num)
            return

        if num > self.minh[0]:
            heapq.heappush(self.minh, num)
        else:
            heapq.heappush(self.maxh, -1*num)

        if abs(len(self.maxh) - len(self.minh)) > 1:
            if len(self.maxh) > len(self.minh):
                heapq.heappush(self.minh, heapq.heappop(self.maxh) * -1)
            else:
                heapq.heappush(self.maxh, -1 *heapq.heappop(self.minh))

    def findMedian(self) -> float:
        totalLen = len(self.maxh) + len(self.minh)
        if totalLen % 2 != 0:
            if len(self.minh) > len(self.maxh):
                return self.minh[0]
            else:
                return self.maxh[0] * -1
        else:
            return (self.minh[0] + (self.maxh[0] * -1)) /2




        
        