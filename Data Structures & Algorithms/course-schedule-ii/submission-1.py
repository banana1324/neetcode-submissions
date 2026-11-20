class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            prereq[a].append(b)
        result = []
        visiting = set()
        visited = set()

        def dfs(course):

            if course in prereq[course]:
                return False

            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)
            
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            visited.add(course)
            result.append(course)
            visiting.remove(course)
            return True
       # print(result)
            
        for x in range(numCourses):
            if not dfs(x):
                return []
        return result