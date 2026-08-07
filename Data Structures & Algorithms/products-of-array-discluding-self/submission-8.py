class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        #output.append(0)
        premulti = nums[0]
        length = len(nums)

        for x in range(0,length):
            if x == 0:
                output.append(1)
            else:
                output.append(premulti)
                premulti *= nums[x]

        postmulti = nums[length-1]
        for x in range(length-2, -1, -1):

            output[x] = output[x] * postmulti
            postmulti *= nums[x]
        return output
