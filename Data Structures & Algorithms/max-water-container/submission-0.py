class Solution:
    def maxArea(self, heights: List[int]) -> int:
        big = 0

        leng = len(heights)

        l = 0
        r = leng -1

        while l < r:
            big = max(big,(r-l) * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return big