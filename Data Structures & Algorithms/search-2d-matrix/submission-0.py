class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binsearch(array,left, right):
            if left > right:
                return -1
            
            midIndx = (left + right) // 2

            if array[midIndx] == target:
                print(array[midIndx])
                return True
            elif array[midIndx] > target:
                return binsearch(array,left, midIndx -1)
            else:
                return binsearch(array,midIndx + 1, right)
        
        xlen = len(matrix)
        ylen = len(matrix[0])

        for array in matrix:
            if binsearch(array,0, len(array) -1) == True:
                return True
        return False