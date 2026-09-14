class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = set()
        left = 0
        right = 0
        while right - left <= k and right < len(nums):
            if nums[right] in seen:
                return True
            else:
                seen.add(nums[right])
                right += 1

        while right < len(nums):
            seen.discard(nums[left])
            left += 1
            if nums[right] in seen:
                return True
            else:
                seen.add(nums[right])
            right += 1
        return False