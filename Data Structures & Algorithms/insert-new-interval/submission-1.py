class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        last = -1
        
        
        for x in range(len(intervals)):
            if intervals[x][1] < newInterval[0]:
                output.append(intervals[x])
            else:
                last = x
                break
        if last == -1:
            return intervals + [newInterval]

        if intervals[last][0] <= newInterval[1]:
            # The intervals overlap
            newInterval[0] = min(newInterval[0], intervals[last][0])
            newInterval[1] = max(newInterval[1], intervals[last][1])
            curr = last
        else:
            # The intervals don't overlap
            curr = last - 1

        while curr + 1 < len(intervals) and intervals[curr + 1][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[curr + 1][1])
            curr += 1
        return output + [newInterval] + intervals[curr+1:]
            






