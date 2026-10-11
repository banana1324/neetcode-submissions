class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        largest = 0
        size = 0
        def go(x,y):
            #if grid[x][y] == 0:
                #return 0

            grid[x][y] = 0
            size = 1

            if x + 1 < len(grid) and grid[x + 1][y] == 1:
                size += go(x + 1,y)
            if x - 1 >=0 and grid[x - 1][y] == 1:
                size += go(x - 1,y)
            if y + 1 < len(grid[0]) and grid[x][y + 1] == 1:
                size += go(x,y + 1)
            if y - 1 >= 0 and grid[x][y - 1] == 1:
                size += go(x,y-1)
            return size

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    size = go(x,y)
                largest = max(largest,size)
                size = 0
        return largest

            
