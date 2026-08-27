class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #bruteforce
        out = [0] * len(temperatures)
        stack = [] #indices of unresolved days

        for currDayInd, currTemp in enumerate(temperatures):
            while stack and currTemp > temperatures[stack[-1]]:
                prevDayInd = stack.pop()
                out[prevDayInd] = currDayInd - prevDayInd
            stack.append(currDayInd)
        return out