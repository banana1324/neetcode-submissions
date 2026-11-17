class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}

        #node : nodes it is adjacent to
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        stack = [0]
        count = 0

        for node in adj:
            if not node in visited:
                stack = [node]
                while stack:
                    curr = stack.pop()
                    
                    if curr in visited:
                        continue
                    
                    visited.add(curr)

                    for neighbor in adj[curr]:
                        stack.append(neighbor)
                
                count += 1
        return count

