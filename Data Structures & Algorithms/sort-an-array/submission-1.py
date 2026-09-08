class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #mergesort!!!

        def mergeSort(array):
            if len(array) <= 1:
                return array
            left= array[:len(array)//2]
            right = array[len(array)//2:]

            left = mergeSort(left)
            right = mergeSort(right)

            return merge(left,right)
        
        def merge(left, right):
            ret = []

            while left and right:
                if left[0] < right[0]:
                    ret.append(left[0])
                    left = left[1:]
                else:
                    ret.append(right[0])
                    right = right[1:]
            
            while left:
                ret.append(left[0])
                left = left[1:]
            while right:
                ret.append(right[0])
                right = right[1:]
            return ret
        return mergeSort(nums)