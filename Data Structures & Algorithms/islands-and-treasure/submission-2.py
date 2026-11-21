from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        #start at treasure and go backwards, labeling every land with its distance
        q = deque([])
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    print(x,y)
                    q.append([x,y,0])
                    visited.add((x,y))
        


        while q:
            curr = q.popleft()
            x = curr[0]
            y = curr[1]
            dist = curr[2]
            
            if not (x-1,y) in visited and x-1 >= 0 and grid[x-1][y] != -1:
                q.append([x-1,y, dist + 1])
                visited.add((x-1,y))

            if not (x,y-1) in visited and y-1 >= 0 and grid[x][y-1] != -1:
                q.append([x,y-1, dist + 1])
                visited.add((x,y-1))

            if not (x + 1,y) in visited and  x + 1 < len(grid) and grid[x + 1][y] != -1:
                q.append([x + 1,y, dist + 1])
                visited.add((x+1,y))

            if not (x,y+1) in visited and  y+1 < len(grid[0]) and grid[x][y+1] != -1:
                q.append([x,y+1, dist + 1])
                visited.add((x,y+1))

            grid[x][y] = min(grid[x][y], dist)


            
