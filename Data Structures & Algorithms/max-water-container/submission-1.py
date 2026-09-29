class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left = 0
        right = len(heights)-1

        while right > left:
            if heights[left] < heights[right]:
                res = max(res, (right-left) * heights[left])
                left += 1
            else:
                res = max(res, (right - left) * heights[right])
                right -= 1
        return res