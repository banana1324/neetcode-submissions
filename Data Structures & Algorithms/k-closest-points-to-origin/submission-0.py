class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distancesMap = {} # distance to point
        distances = [] #distance i will sort

        for point in points:
            dist =  ((point[0] **2) + (point[1] ** 2)) ** 0.5
            distances.append([dist, point])
            
        
        distances = sorted(distances, key = lambda x : x[0])
        print(distances)
        ret = []
        for x in range(k):
            ret.append(distances[x][1])
        
        return ret