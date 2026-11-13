class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                output[y][x] = matrix[x][y]
        return output