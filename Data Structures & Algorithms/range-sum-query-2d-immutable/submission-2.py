class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        #find pref sum of every row
        self.matrixPrefSum = []
        for row in matrix:
            curr = 0
            currList = []
            for x in range(len(row)):
                currList.append(curr)
                curr += row[x]
            self.matrixPrefSum.append(currList)
        print (self.matrixPrefSum)
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1,row2 + 1):
            #sum of each row
            res += self.matrixPrefSum[row][col2] - self.matrixPrefSum[row][col1]
            res += self.matrix[row][col2]
        return res
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)