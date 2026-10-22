from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        store = []
        for x in range(m):
            curr = []
            for x in range(n):
                curr.append(0)
            store.append(curr)


        store[m-1][n-1] = 1
        q = deque([]) #x,y
        seen = set([m-1,n-1])
        if m != 1: 
            q.append(([m-2,n-1]))
            seen.add((m-1,n-1))

        if n != 1: 
            q.append([m-1,n-2])
            seen.add((m-1,n-2))
        
        
        while q:
            curr = q.popleft()

            if curr[0] - 1 >= 0 and (curr[0]-1,curr[1]) not in seen:
                q.append([curr[0] - 1, curr[1]])
                seen.add((curr[0] - 1, curr[1]))

            if curr[1] - 1 >= 0 and (curr[0],curr[1] - 1) not in seen:
                q.append([curr[0], curr[1] - 1])
                seen.add((curr[0],curr[1]-1))
                
            zum = 0
            if curr[0] + 1 < m:
                zum += store[curr[0] + 1][curr[1]]

            if curr[1] + 1 < n:
                zum += store[curr[0]][curr[1] + 1]

            store[curr[0]][curr[1]] = zum
        return store[0][0]



