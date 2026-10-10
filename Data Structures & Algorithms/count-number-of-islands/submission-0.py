class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #find a one, and turn every surrounding one into a zero

        def found(x,y):
            if x < len(grid) and y < len(grid[0]) and grid[x][y] != "0":
                print(x)
                print(y)
                grid[x][y] = "0"

                if x + 1 < len(grid):
                    found(x + 1,y)
                if x - 1 >= 0:
                    found(x-1,y)
                if y + 1 < len(grid[0]):
                    found(x,y+1)
                if y - 1 >=0:
                    found(x,y-1)
                

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    res += 1
                    found(x,y)
        return res