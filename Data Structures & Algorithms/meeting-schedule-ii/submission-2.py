"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        q = []
        intervals.sort(key = lambda x: x.start)

        for interval in intervals:
            if not q:
                heapq.heappush(q, interval.end)
            else:
                if q[0] > interval.start:
                    heapq.heappush(q, interval.end)
                else:
                    heapq.heappop(q)
                    heapq.heappush(q,interval.end)
        return len(q)