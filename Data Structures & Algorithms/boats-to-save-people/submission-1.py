from collections import deque
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        people = deque(people)

        boats = 0
        while people:
            curr = people.pop()
            if people and people[0] + curr <= limit:
                curr += people.popleft()
            boats += 1
        return boats

        #3,3,4,5