class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        biggest = 0
        for number in setnums:
            if number - 1 not in setnums:
                leng = 1
                curr = number
                while True:
                    if curr + 1 in setnums:
                        leng += 1
                        curr += 1
                    else:
                        if biggest < leng:
                            biggest = leng
                        break
                            
        return biggest