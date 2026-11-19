class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            prereq[a].append(b)

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
            visiting.remove(course)
            return True
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True